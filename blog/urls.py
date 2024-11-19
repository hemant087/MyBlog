from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('get-blog/<id>/', views.get_blog, name='get_blog'),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('register/', views.user_register, name = "register"),
    path('create_blog/',views.create_blog, name = "create_blog"),
    path('update_blog/',views.update_blog, name = "update_blog"),
    path('delete_blog/<id>/',views.delete_blog, name = "delete_blog"),
    path('show-all-blogs/', views.show_all_blogs, name = "show-all-blogs"),
]
