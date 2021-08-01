from django.contrib.postgres.fields import ArrayField
from typing import AbstractSet, Text
from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    user_name=models.CharField(max_length=50)                                       #실명
    user_nickname=models.CharField(max_length=50)                                   #닉네임
    user_id=models.EmailField(max_length=50, unique=True, primary_key=True)         #아이디
    user_password=models.CharField(max_length=50, unique=True)                      #비밀번호
    user_phone_number=models.CharField(max_length=12)                               #전화번호
    user_link=models.URLField()                                                     #계정(반려견 계정:인스타, 페이스북,트위터)


   
class Animal(models.Model):

    animal_id = models.IntegerField(primary_key=True)                               # 동물 고유 id
    
    name = models.CharField(max_length=50)                                          # 동물 이름
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)                    # 주인 id
    species = models.CharField(max_length=50)                                       # 상위 종류
    subspecies = models.CharField(max_length=50)                                    # 하위 종류
    profile_photo = models.ImageField(upload_to='static/profile_photo/', null=True) # 프로필 사진
    birthday = models.DateField()                                                   # 탄생일
    memorialday = models.DateField()                                                # 제삿날
    introduce = models.TextField()                                                  # 소개글
    season = models.CharField(max_length=10)                                        # 제일 좋아한 계절                         
    flowers = ArrayField(                                                           # 꽃다발 이름 저장될 배열 
            models.CharField(max_length=10, blank=True),
            size=8
            ) 
    gravestone = models.CharField(max_length=50)                                    # 묘비
    

  
class Diary(models.Model): # 하루를 들려줄게
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    diary_title = models.CharField(max_length=100)
    diary_pub_date = models.DateTimeField()
    diary_body=models.TextField()
    
    
class Gallery(models.Model): # 갤러리
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    gallery_image = models.ImageField(upload_to = "gallery/", blank = True, null = True)

    
class VisiterBook(models.Model): #방명록
<<<<<<< HEAD
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    visbook_title = models.CharField(max_length=100)
    visbook_pub_date = models.DateTimeField()
    visbook_body=models.TextField()
    visbook_reply=models.TextField()
=======
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    visitor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body=models.TextField()
    reply=models.TextField()
>>>>>>> b89c1972b3e0c54c20d3f13014ffee6ef6fe7187
    
class csCenter(models.Model):
    title=models.CharField(max_length=100)                                #제목
    text=models.TextField()                                 #내용
    register_date=models.DateField                          #작성날짜
    writer=models.CharField(max_length=50)                  #작성자

