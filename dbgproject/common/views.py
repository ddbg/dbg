from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import * 

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            user_id = request.POST["user_id"]
            user_password= request.POST["user_password"]
            user = authenticate(request=request,user_id=user_id, user_password=user_password)
            if user is not None:
                login(request, user)
        return redirect("home")

    else:
        form=AuthenticationForm()
        return render(request, "login.html")
         


def logout_view(request):
    logout(request)
    return redirect("home")

def signUp(request):
     if request.method == 'POST':
         form=AuthenticationForm(request=request,data = request.POST)
         if form.is_valid():
             user = form.save()
             login(request,user)
         return redirect("home")
             
     else:
         form: UserCreationForm
         return render(request, "signUp.html")
    
