from django.db import models

# Create your models here.
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
    #restaurant_name = models.ForeignKey('Restaurant',null=True, on_delete=models.SET_NULL)
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
    #rest_name = models.ForeignKey('Restaurant',on_delete=models.SET_NULL,null=True)
    item_img = models.ImageField(upload_to='items/images',default='')
    item_name = models.CharField(max_length=100,null=True)
    item_price = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    category = models.CharField(max_length=100,choices=food_category, null=True)
    #category = models.ForeignKey('FoodCategory',null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.item_name