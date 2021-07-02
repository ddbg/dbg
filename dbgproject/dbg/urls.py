from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [    
    path('', home, name="home"),
    path('honor/',honor, name="honor"),
    path('honorRegister/',honorRegister, name="honorRegister"),
    path('honorRegistered/',honorRegistered, name="honorRegistered"),
    path('free/', free, name="free"),
    path('freeRegister/',freeRegister, name="freeRegister"),
    path('freeRegistered/',freeRegistered, name="freeRegistered"),
    path('aboutUs/',aboutUs, name="aboutUs"),
    path('searchMap/',searchMap,name="searchMap"),
    path('searchResult/',searchResult, name='searchResult'),
    path('mypage/',mypage,name="mypage"),
    path('mypageDiary/',mypageDiary,name="mypageDiary"),
    path('mypagePhoto/',mypagePhoto,name="mypagePhoto"),
    path('test/',test,name="test"),path('enroll/',enroll, name="enroll"),
    path('enroll/',enroll, name="enroll"),
    path('enroll2/',enroll2, name="enroll2"),
    path('caaard/', caaard, name="caaard"),
] 
