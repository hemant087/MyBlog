from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('get-blog/<id>/', get_blog, name='get_blog'),
    path('login/', user_login, name = "login"),
    path('logout/', user_logout, name = "logout"),
    path('register/', user_register, name = "register"),
]
