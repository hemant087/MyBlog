from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')

def user_login(request):
    return render(request,'user_login.html')

def user_logout(request):
    return render(request,'user_logout.html')

def user_register(request):
    return render(request,'user_register.html')

def get_blog(request, id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id= id)
        context['blog'] = blog_obj
    except Exception as ex:
        print(ex)
    return render(request, 'views_blog.html', context)