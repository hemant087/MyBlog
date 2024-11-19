from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'index.html')


def user_login(request):
    return render(request, 'user_login.html')


def user_logout(request):
    return redirect('/')


def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')



        user_obj = User.objects.filter(username = username)
        if user_obj.exists():
            messages.warning(request, 'Username is already taken !')
            return redirect('/register/')

        user_obj = User.objects.filter(email = email)
        if user_obj.exists():
            messages.warning(request, 'This Email Add. already exist !')
            return redirect('/register/')
        
        user_obj = User(username = username, email = email)
        user_obj.set_password(password)
        return redirect('/login/')


    return render(request, 'user_register.html')

def create_blog(request):
    return render(request, 'create_blog.html')
def update_blog(request):
    return render(request, 'update_blog.html')
def delete_blog(request):
    return redirect(request, '/')

def show_all_blogs(request):
    return render(request, 'show_all_blogs.html')


def get_blog(request, id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id=id)
        context['blog'] = blog_obj
    except Exception as ex:
        print(ex)
    return render(request, 'views_blog.html', context)
