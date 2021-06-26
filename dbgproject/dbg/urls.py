from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home, name="home"),
    path('free/', free, name="free"),
    path('freeRegister/',freeRegister, name="freeRegister"),
    path('freeRegistered/',freeRegistered, name="freeRegistered"),
    path('aboutUs/',aboutUs, name="aboutUs"),
    path('searchMap/',searchMap,name="searchMap"),
]