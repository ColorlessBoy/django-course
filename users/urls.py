from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.userpage, name="user"),
    path('register', views.registerpage, name="register"),
    path('login', views.loginpage, name="login"),
    path('logout', views.logoutpage, name="logout"),
]
