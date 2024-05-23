# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("<h1> Home Page </h1>")
    return render(request, 'home.html')

def aboutpage(request):
    # return HttpResponse("<h1> About Page </h1>")
    return render(request, 'about.html')