
from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)


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


    # 방명록
    
    # 하루를 들려줄게

    # 갤러리

  

    
     
