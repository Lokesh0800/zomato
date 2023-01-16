from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from zapp.models import Order
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
User = get_user_model() 

# Create your views here.

def homepage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            user = User.objects.get(email=email)
            success = user.check_password(password)
            print(user.is_staff,user.is_active)
            if success:
                if user.is_superuser:
                    print('executed')
                    
                    return redirect('restpage')
                else:
                    pass
        except Exception as e:
            print('aaaaaaaaaa')
            print(e)

    return render(request, 'rest.html')

@staff_member_required(login_url='homepage')
def restpage(request):
    print('Running')
    return render(request,'restindex.html')
