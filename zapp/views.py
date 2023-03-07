#from email import message
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from zapp.models import *
from math import ceil
import random,requests,json
from django.core import serializers 
from django.conf import settings  
#from django.contrib.auth.models import User
from .models import User
from .custauthuser import authenticate
from Restaurant.models import RestAddress,Menuitems,FoodCategory

#User = settings.AUTH_USER_MODEL     

# Create your views here.

def send_otp_tophone(request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        otp=''
        try:
            User.objects.get(phone_number=phone)
            #msg = messages.error(request, 'Phone number already registered')            
            return HttpResponse("mob_exist")
        except:
            try:
                User.objects.get(username=username)
                #msg = messages.error(request, 'Username already registered')
                return HttpResponse("user_exist")
            except:
                try:
                    User.objects.get(email=email)
                    #msg = messages.error(request, 'Email already registered')
                    return HttpResponse("email_exist")
                except:
                    mob = request.POST['phone']
                    otp =  random.randint(1000,9999) 
                    print(otp)
                    #url = f'https://2factor.in/API/V1/254860ba-68b0-11ed-9c12-0200cd936042/SMS/{mob}/{otp}/'
                    #response = requests.get(url)
                    #msg = messages.success(request, 'User successfully registered')
                    return HttpResponse(otp)

def homepage(request):  
    Address = RestAddress.objects.all()
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("pass")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        entered_otp = request.POST.get("otp")
        generated_otp = request.POST.get("generated_otp")
        print(generated_otp)
        if entered_otp == generated_otp:
            try:
                if User.myobj.filter(username=username).exists():
                    msg = messages.error(request, 'Username already exist')
                    return redirect('/', {'message': msg,'address':Address})
                else:
                    if User.myobj.filter(email=email).exists():
                        msg = messages.error(request, 'Email already exist')
                        return redirect('/', {'message': msg,'address':Address})
                    else:
                        myuser = User.myobj.create(username = username,email=email,phone_number=phone,is_verified=True)
                        myuser.first_name = fname
                        myuser.last_name = lname
                        myuser.set_password(password)
                        myuser.save()   
                        msg = messages.success(
                            request, f'Account with username {username} successfully created')
                        return HttpResponseRedirect('/', {'message': msg,'address':Address})
            except Exception as e:               
                msg = messages.success(
                    request, "Incorrect Credential, Please fill the form correctly")
                return HttpResponseRedirect('/', {'message': msg,'address':Address})
        else:
            msg = messages.error(request, 'Incorrect OTP')
            return HttpResponseRedirect('/', {'message': msg,'address':Address})
    else:
        return render(request, 'index.html',{'address':Address})

def loginpage(request):
    
    if request.method == 'POST':
        phone_number = request.POST.get("phone_number")
        loginpass = request.POST.get("loginpass")
        try:
            user = authenticate(phone=phone_number, password=loginpass)
            if user is not None:
                login(request, user)    
                return redirect('userpage')
            else:
                msg = messages.error(
                    request, 'Login Unsuccessfull, Please check username and password ')
                return HttpResponseRedirect('/', {'message': msg})
        except Exception as e:
            msg = messages.error(request, 'Login Unsuccessfull')
            return HttpResponseRedirect('/', {'message': msg})
    else:
        msg = messages.error(request, 'Login to Continue')
        return HttpResponseRedirect('/', {'message': msg})

@login_required(login_url='home')
def userpage(request):
    key = settings.GOOGLE_API_KEY

    if request.method == 'POST':
        house = request.POST.get('house')
        street = request.POST.get('street')
        locality = request.POST.get('locality')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        address = UserAddress(user=request.user, house=house,
                              street_no=street, locality=locality, city=city, pincode=zip)
        address.save()
    myuser = request.user.get_username()
    userobj = User.objects.get(phone_number=myuser)
    address = UserAddress.objects.filter(user=userobj)
    restaurant_address = RestAddress.objects.all().values()
    restaurant_locality = RestAddress.objects.values('locality')    
    items = Menuitems.objects.all().values()
    food_category = FoodCategory.objects.all().values()
    pizza_burger = Menuitems.objects.filter(category='Pizza and Burgers').values()
    italian = Menuitems.objects.filter(category='Italian').values()
    sandwich = Menuitems.objects.filter(category='Breakfast').values()
   
    # n1 = len(pizza_burger)
    # n2 = len(italian)
    # n3 = len(sandwich)
    # ns1 = n1//4 + ceil((n1/4)-(n1//4))
    # ns2 = n2//4 + ceil((n2/4)-(n2//4))
    # ns3 = n3//4 + ceil((n3/4)-(n3//4))
    # pizzaburger = [(pizza_burger, range(1, ns1), ns1),(italian, range(1, ns2), ns2), (sandwich, range(1, ns3), ns3),]
    # italian = [(italian, range(1, ns2), ns2), ]
    # sandwiches = [(sandwich, range(1, ns3), ns3), ]

    return render(request, 'home.html',
                  {
                      'user':userobj,
                      'locality': restaurant_locality,
                      'address': restaurant_address,
                      'items': items,
                      'pizzaburger': pizza_burger,
                      'italian': italian,
                      'sandwiches': sandwich,
                      'cat':food_category,
                      'myaddress': address,
                      'key':key,
                  }
                  )

def logouthandle(request):
    logout(request)
    msg = messages.success(request, 'Successfully Loged Out')
    return redirect('home')

@login_required(login_url='home')
def orderpage(request):
    myuser = request.user.get_username()
    userobj = User.objects.get(phone_number=myuser)
    myorder = Order.objects.filter(username=userobj).order_by('-datetime').values('datetime','useraddress','orderid','totalprice')
    orderitem = Order.objects.filter(username=userobj).order_by('-datetime').values('items')
    ord = (len(orderitem))
    for i in orderitem:
        for j in i:
            i[j] = (eval(i[j]))
    items = zip(myorder,orderitem)
    # orderitems = (eval(myorder[1]["items"]))
    # items = [(myorder,orderitems)]
    return render(request,'orderpage.html',{'myorder':items,'len':ord})

@login_required(login_url='home')
def checkout(request):
    try:
        myuser = request.user.get_username()
        userobj = User.objects.get(phone_number=myuser)
        address = UserAddress.objects.filter(user=userobj)
        if request.method == 'POST':
            orderitem = json.loads((request.POST.get("itemsJson")))
            useradd = json.loads((request.POST.get("addressJson")))
            total = request.POST.get('total')
            myorder = Order.objects.create(useraddress=useradd, items=orderitem,totalprice=total)
            myorder.username = request.user
            myorder.save()  
            msg = messages.success(request, 'Order Placed')
            return HttpResponseRedirect('userpage', {'address': useradd, 'user': userobj,'message': msg})
        else:
            return render(request, 'checkout.html', {'myaddress': address})
    except:
        msg = messages.error(request, 'Please select Delivery Address')
        return HttpResponseRedirect('checkout', { 'user': userobj,'message': msg})

def google_mapp(request):
    return render(request,'mapp.html')