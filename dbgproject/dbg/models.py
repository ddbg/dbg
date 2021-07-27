from typing import AbstractSet, Text
from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import AbstractUser

# Create your models here.


   
class User(models.Model):
    user_name=models.CharField(max_length=50)                                       #실명
    user_nickname=models.CharField(max_length=50)                                   #닉네임
    user_id=models.EmailField(max_length=50, unique=True, primary_key=True)         #아이디
    user_password=models.CharField(max_length=50, unique=True)                      #비밀번호
    user_phone_number=models.CharField(max_length=12)                               #전화번호
    user_link=models.URLField()                                                     #계정(반려견 계정:인스타, 페이스북,트위터)


class csCenter(models.Model):
    title=models.CharField(max_length=100)                                #제목
    text=models.TextField()                                 #내용
    register_date=models.DateField                          #작성날짜
    writer=models.CharField(max_length=50)                  #작성자

