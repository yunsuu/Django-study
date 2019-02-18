from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    Blogs = Blog.objects
    return render(request,'home.html',{'blogs':Blogs})