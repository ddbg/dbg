from django.shortcuts import render, redirect
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.db.models import Q
from .forms import AnimalForm
from .models import * 

def home(request):

    # 오늘 월, 일 계산
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    day=today[2:]
    return render(request, "home.html",{"month":month, "day":day})

def honor(request):
    return render(request,"honor.html") 

def honorRegister1(request):
    return render(request, "honorRegister1.html")

def honorRegister2(request):

    newHonorAnimal = Animal()
    newHonorAnimal.name = request.POST['animalName']

    return render(request, "honorRegister2.html",{'honorAnimal':newHonorAnimal})

def honorRegistered(request):
    return redirect('honor')

def free(request):

    # 오늘 월, 일 계산
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    month = month.rjust(2, '0')
    day=today[2:]

    free_animals = Animal.objects.filter(
        category = "free"
    )

    today_stars = Animal.objects.filter(
        memorialday__month = month,
        memorialday__day = day
    )
   
    return render(request, "free.html",{"month":month, "day":day, 'free_animals': free_animals,'empty_num':4-len(free_animals)%4,
     'today_stars': today_stars, 'today_stars_num': len(today_stars) })

def freeRegister1(request):
    return render(request, "freeRegister1.html")

def freeRegister2(request):
    newFreeAnimal = Animal()

    temp_id = Animal.objects.count()
    newFreeAnimal.animal_id = temp_id +1 if temp_id != 0 else 1
    #newFreeAnimal.owner_id = request.POST['']
    newFreeAnimal.category = 'free'
    newFreeAnimal.name = request.POST['animalName']
    newFreeAnimal.species = request.POST['animalType']
    newFreeAnimal.subspecies = request.POST['animalSubType']
    newFreeAnimal.birthday = request.POST['animalBirthDay']
    newFreeAnimal.memorialday = request.POST['animalMemorialDay']
    newFreeAnimal.profile_photo = request.POST['animalImg']
    newFreeAnimal.introduce = request.POST['animalInfo']

    newFreeAnimal.save()

    return render(request, "freeRegister2.html",{'freeAnimal':newFreeAnimal})

def freeRegistered(request, animal_id):
    newFreeAnimal = Animal.objects.get(animal_id=animal_id)
    newFreeAnimal.season = request.POST['animalSeason']
    newFreeAnimal.flowers = request.POST['animalFlower']
    newFreeAnimal.gravestone = request.POST['animalGravestone']
    newFreeAnimal.pub_date = datetime.now()
    newFreeAnimal.save()
    
    return redirect('free')

def enroll(request):
    return render(request, "enroll.html")

def enroll2(request):

    newAnimal = Animal()
    newAnimal.name = request.POST['animalName']
    
    return render(request, "enroll2.html",{'animal':newAnimal})

def enrolled(request):
    return redirect('home')


def caaard(request):
    return render(request, "caaard.html")

def aboutUs(request):
    return render(request, "aboutUs.html")

def searchMap(request):
    return render(request, "searchMap.html")

def searchResult(request):
    searchWord=request.POST['searchInput']

    animals = Animal.objects.filter(
        Q(name__contains = searchWord)|
        Q(category__contains = searchWord)|
        Q(species__contains = searchWord)|
        Q(subspecies__contains = searchWord)|
        Q(birthday__contains = searchWord)|
        Q(memorialday__contains = searchWord)|
        Q(introduce__contains = searchWord)
    )
    return render(request, "searchResult.html",{"searchWord":searchWord, "animals":animals
    , "animals_num": len(animals), "empty_num":4-len(animals)%4})


def mypage(request):
    return render(request, "mypage.html")

def mypageDiary(request):
    return render(request, "mypageDiary.html")

def mypagePhoto(request):
    return render(request, "mypagePhoto.html")

def mypageVisitorBook(request):
    return render(request, "mypageVisitorBook.html")  

def login_view(request):
    return render(request, "login.html")


def logout_view(request):
    return redirect("home")

def csCenter(request):
    return render(request, "csCenter.html")    

def signUp(request):
    return render(request, "signUp.html")

def q_and_a(request):
    return render(request, "q_and_a.html")    

def idFind(request):
    return render(request, "idFind.html")    

def pwFind(request):
    return render(request, "pwFind.html")    

def normal(request):
    return render(request, "normal.html")