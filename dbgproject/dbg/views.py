from django.shortcuts import render, redirect
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.db.models import Q
from .forms import AnimalForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import * 
from django.core.paginator import Paginator

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

    # 카테고리가 free인 동물들만 가져와 free_animals에 저장
    free_animals = Animal.objects.filter(
        category = "free"
    )

    # 오늘 월/일에 죽은 동물들만 가져와 today_starts에 저장
    today_stars = Animal.objects.filter(
        memorialday__month = month,
        memorialday__day = day
    )
   
    # 한 페이지 당 16마리 동물 보이도록 페이지네이션
    paginator = Paginator(free_animals, 16)
    page = request.GET.get('page')          # 몇번째 페이지인지 받아옴

    free_animals = paginator.get_page(page)

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
    newFreeAnimal.profile_photo = request.FILES.get('animalImg', None)
    newFreeAnimal.introduce = request.POST['animalInfo']

    newFreeAnimal.save()

    return render(request, "freeRegister2.html",{'freeAnimal':newFreeAnimal})

def freeRegistered(request, animal_id):
    newFreeAnimal = Animal.objects.get(animal_id=animal_id)
    newFreeAnimal.season = request.POST['animalSeason']
    newFreeAnimal.flowers = request.POST['animalFlower']
    newFreeAnimal.gravestone = request.POST['animalGrovestone']
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