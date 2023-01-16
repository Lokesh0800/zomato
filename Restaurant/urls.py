
from django.urls import path
from Restaurant import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('restpage',views.restpage,name='restpage'),
    
]