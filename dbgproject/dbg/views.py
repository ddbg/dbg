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

def honorRegister(request):
    return render(request, "honorRegister.html")


def honorRegistered(request):
    return redirect('honor')


def freeRegister(request):
    return render(request, "freeRegister.html")


def freeRegistered(request):
    return redirect('free')

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

