from django.db import models


class User(models.Model):
    user_id=models.EmailField(max_length=50, unique=True, primary_key=True)         #아이디
    
    user_name=models.CharField(max_length=50)                                       #실명
    user_nickname=models.CharField(max_length=50, unique=True)                      #닉네임
    user_password=models.CharField(max_length=50)                                   #비밀번호
    user_phone_number=models.CharField(max_length=12)                               #전화번호
    user_link=models.URLField()                                                     #계정(반려견 계정:인스타, 페이스북,트위터)


   
class Animal(models.Model):

    animal_id = models.IntegerField(primary_key=True)                               # 동물 고유 id
    
    name = models.CharField(max_length=50)                                          # 동물 이름
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)                    # 주인 id
    category = models.CharField(max_length=50)                                       # 카테고리 
    species = models.CharField(max_length=50)                                       # 상위 종류
    subspecies = models.CharField(max_length=50, null=True)                         # 하위 종류
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True) # 프로필 사진
    birthday = models.DateField(null=True)                                          # 탄생일
    memorialday = models.DateField()                                                # 제삿날
    introduce = models.TextField(null=True)                                         # 소개글
    season = models.CharField(max_length=10, null=True)                             # 제일 좋아한 계절                         
    flowers = models.CharField(max_length=200, null=True)                           # 꽃다발
    gravestone = models.CharField(max_length=50, null=True)                                    # 묘비
    pub_date = models.DateTimeField(null=True)                                                # 등록시간
    

  
class Diary(models.Model): # 하루를 들려줄게
    diary_id = models.IntegerField(primary_key=True)  
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    diary_title = models.CharField(max_length=100)
    diary_pub_date = models.DateTimeField()
    diary_body=models.TextField()
    
    
class Gallery(models.Model): # 갤러리
    gallery_id= models.IntegerField(primary_key=True)  
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    gallery_image = models.ImageField(upload_to = "gallery/", blank = True, null = True)

    
class VisiterBook(models.Model): #방명록
    vs_id = models.IntegerField(primary_key=True)  
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    visbook_title = models.CharField(max_length=100)
    visbook_pub_date = models.DateTimeField()
    visbook_body=models.TextField()
    visbook_reply=models.TextField()
    
class csCenter(models.Model):
    cs_id = models.IntegerField(primary_key=True)  
    title=models.CharField(max_length=100)                                #제목
    text=models.TextField()                                 #내용
    register_date=models.DateField                          #작성날짜
    writer=models.CharField(max_length=50)                  #작성자

