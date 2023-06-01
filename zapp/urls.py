from django.contrib import admin
from django.urls import path
from zapp import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('mypage',views.loginpage, name='loginpage'),
    path('userpage',views.userpage,name='userpage'),
    path('logout',views.logouthandle,name='logouthandle'),
    path('order',views.orderpage,name='orderpage'),
    path('checkout',views.checkout,name='checkout'),
    path('google_mapp',views.google_mapp,name='google_mapp'),
    path('send_otp_tophone',views.send_otp_tophone,name='send_otp_tophone'),
    path('payment-success',views.success,name='success')    
]

