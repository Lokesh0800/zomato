from django.contrib import admin
from Restaurant.models import DeliveryBoy,RestAddress,Menuitems,FoodCategory

# Register your models here.
admin.site.register(DeliveryBoy)
admin.site.register(RestAddress)
admin.site.register(Menuitems)
admin.site.register(FoodCategory)