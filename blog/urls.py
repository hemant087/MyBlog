from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('get-blog/<id>/', get_blog, name='get_blog')
]
