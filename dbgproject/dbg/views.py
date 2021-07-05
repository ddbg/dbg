from django.shortcuts import render, redirect
from datetime import datetime
from django.utils.dateformat import DateFormat
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
    return render(request, "honorRegister2.html")


def honorRegistered(request):
    return redirect('honor')


def freeRegister1(request):
    return render(request, "freeRegister1.html")

def freeRegister2(request):
    return render(request, "freeRegister2.html")

def freeRegistered(request):
    return redirect('free')

def enroll(request):
    return render(request, "enroll.html")

def enroll2(request):
    return render(request, "enroll2.html")

def enrolled(request):
    return redirect('home')

def caaard(request):
    return render(request, "caaard.html")

def free(request):

    # 오늘 월, 일 계산
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    day=today[2:]
    
    return render(request, "free.html",{"month":month, "day":day})

def aboutUs(request):
    return render(request, "aboutUs.html")

def searchMap(request):
    return render(request, "searchMap.html")

def searchResult(request):

    searchWord=request.POST['searchInput']

    return render(request, "searchResult.html",{"searchWord":searchWord})


def mypage(request):
    return render(request, "mypage.html")

def mypageDiary(request):
    return render(request, "mypageDiary.html")

def mypagePhoto(request):
    return render(request, "mypagePhoto.html")

def login(request):
    return render(request, "login.html")    

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