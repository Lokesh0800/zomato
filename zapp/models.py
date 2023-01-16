from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields
from .managers import mymanager
from django.conf import settings

User = settings.AUTH_USER_MODEL

class DeliveryBoy(models.Model):
    enp_id = models.CharField(max_length=10,null=True)
    boy_name = models.CharField(max_length=100,null=True)
    boy_mob = models.CharField(max_length=100,null=True)
    boy_vehicle = models.CharField(max_length=100,null=True)
    is_occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return (self.boy_name)

food_category = (
    ('Chinese','Chinese'),
    ('South Indian','South Indian'),
    ('Breakfast','Breakfast'),
    ('Ice Cream','Ice Cream'),
    ('Sweets','Sweets'),
    ('Beverage','Beverage'),
    ('Italian','Italian'),
    ('Soups','Soups'),
    ('Starters','Starters'),
    ('Tandoors','Tandoors'),
    ('Main Course','Main Course'),
    ('Rice & Biryanis','Rice & Biryanis'),
    ('Bread','Bread'),
    ('Pizza and Burgers','Pizza and Burgers'),  
)

class FoodCategory(models.Model):
    food_category = models.CharField(max_length=30,null=True,blank=True)
    
    def __str__(self):
        return (self.food_category)


class RestAddress(models.Model):
    
    locality = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=300,null=True)
    city = models.CharField(max_length=20,null=True)
    latitude = models.CharField(max_length=20,null=True,blank=True)
    longitude = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=20,null=True)
    pincode = models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return (self.city +'-'+ self.locality)

class Menuitems(models.Model):
    item_img = models.ImageField(upload_to='items/images',default='')
    item_name = models.CharField(max_length=100,null=True)
    item_price = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    category = models.CharField(max_length=100,choices=food_category, null=True)
    
    
    def __str__(self):
        return self.item_name

class Order(models.Model):
    datetime = models.DateTimeField(default=datetime.datetime.now,null=True)
    orderid = models.AutoField(primary_key=True)
    username = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    useraddress = models.CharField(null=True,max_length = 1000)
    items = models.CharField(null=True,max_length = 5000)
    totalprice = models.CharField(null=True,max_length = 100)

class UserAddress(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    house = models.CharField(max_length=20,null=True)
    street_no = models.CharField(max_length=20,null=True)
    locality = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=20,null=True)
    address = map_fields.AddressField(max_length=200, null='True')
    geolocation = map_fields.GeoLocationField(max_length=100, null='True')
    pincode = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return (self.locality)
    
class Quantity(models.Model):
    quantity = models.IntegerField(null=True,blank=True)
    
class User(AbstractUser):
    phone_number = models.CharField(max_length=10,unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username','email','first_name','last_name','password']
    myobj = mymanager()
    
    def __str__(self):
        return (self.username)
    