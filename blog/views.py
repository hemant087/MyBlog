from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')

def get_blog(request, id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id= id)
        context['blog'] = blog_obj
    except Exception as ex:
        print(ex)
    return render(request, 'views_blog.html', context)