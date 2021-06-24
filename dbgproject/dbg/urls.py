from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    
    path('', home, name="home"),
    path('free/', free, name="free"),
    path('freeRegister/',freeRegister, name="freeRegister"),

]