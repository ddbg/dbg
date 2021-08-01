from django.contrib.postgres.fields import ArrayField
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


   
class Animal(models.Model):

    animal_id = models.IntegerField(primary_key=True)                   # 동물 고유 id
    
    name = models.CharField(max_length=50)          
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)        # 주인 id
    species = models.CharField(max_length=50)                           # 상위 종류
    subspecies = models.CharField(max_length=50)                        # 하위 종류
    profile_photo = models.ImageField(upload_to='static/profile_photo/', null=True)
    birthday = models.DateField()                                       # 탄생일
    memorialday = models.DateField()                                    # 제삿날
    introduce = models.TextField()
    season = models.CharField(max_length=10)                            # 꽃다발 이름 저장될 배열                         # 제일 좋아한 계절
    flowers = ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8
            ) 
    gravestone = models.CharField(max_length=50)                        # 묘비
    
    # models.py의 Blog 클래스 내부 함수
    def __str__(self):
        # 객체 호출 시, 포스팅 제목을 오브젝트 명으로
        return self.name

  
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
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    visbook_title = models.CharField(max_length=100)
    visbook_pub_date = models.DateTimeField()
    visbook_body=models.TextField()
    visbook_reply=models.TextField()
    
class csCenter(models.Model):
    title=models.CharField(max_length=100)                                #제목
    text=models.TextField()                                 #내용
    register_date=models.DateField                          #작성날짜
    writer=models.CharField(max_length=50)                  #작성자

