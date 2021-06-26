from django.shortcuts import render
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.core.paginator import Paginator

def home(request):
    return render(request, "home.html")


def freeRegister(request):
    return render(request, "freeRegister.html")


def free(request):

    # 오늘 월, 일 계산
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    day=today[2:]
    
    return render(request, "free.html",{"month":month, "day":day})

