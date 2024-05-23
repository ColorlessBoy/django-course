from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def userpage(request):
    return HttpResponse("This is User page.")

def registerpage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
    
