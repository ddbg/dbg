from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
        
    path('', home, name="home"),
    path('honor/',honor, name="honor"),
    path('honorRegister1/',honorRegister1, name="honorRegister1"),
    path('honorRegister2/',honorRegister2, name="honorRegister2"),
    path('honorRegistered/<str:animal_id>/',honorRegistered, name="honorRegistered"),
    path('free/', free, name="free"),
    path('freeRegister1/',freeRegister1, name="freeRegister1"),
    path('freeRegister2/',freeRegister2, name="freeRegister2"),
    path('freeRegistered/<str:animal_id>',freeRegistered, name="freeRegistered"),
    path('aboutUs/',aboutUs, name="aboutUs"),
    path('searchMap/',searchMap,name="searchMap"),
    path('searchResult/',searchResult, name='searchResult'),
    path('mypage/',mypage,name="mypage"),
    #path('mypageDiary/',mypageDiary,name="mypageDiary"),
    path('<str:id>',mypageDiary,name="mypageDiary"),
    path('Diarycreate',Diarycreate,name="Diarycreate"),
    path('<str:id>',mypagePhoto,name="mypagePhoto"),
    path('Photocreate',Photocreate,name = "Photocreate"),
    path('mypageVisitorBook/', mypageVisitorBook, name="mypageVisitorBook"),
    path('mypageOption/<str:id>',mypageOption,name="mypageOption"),
    path('mypageUpdate/<str:id>',mypageUpdate,name="mypageUpdate"),
    path('enroll/',enroll, name="enroll"),
    path('enroll2/',enroll2, name="enroll2"),
    path('enrolled/<str:animal_id>',enrolled, name="enrolled"),
    path('caaard/', caaard, name="caaard"),
    path('signUp/', signUp, name="signUp"),
    path('csCenter/', csCenter, name="csCenter"),
    path('q_and_a/', q_and_a, name="q_and_a"),
    path('idFind/', idFind, name="idFind"),
    path('pwFind/', pwFind, name="pwFind"),
    path('normal/',normal, name="normal"),
    path('animal_delete/str:id',animal_delete,name="animal_delete"),
    


] 
