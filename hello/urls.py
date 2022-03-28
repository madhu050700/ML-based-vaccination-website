from django.contrib import admin
from django.urls import path,include
from hello import views


urlpatterns = [

    path('',views.hello, name='hello'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('appointment',views.appointment,name='appointment'),
    path('helpline',views.helpline,name='helpline'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('register',views.register,name='register'),
    path('result',views.result,name='result'),
    path('notification',views.notification,name='notification'),
    

    

]