from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

# Create your views here.

def userpage(request):
    return HttpResponse("This is User page.")

def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("posts:list")
    else: 
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})

def logoutpage(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")
        
def registerpage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
    
