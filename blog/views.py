from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    Blogs = Blog.objects.all()
    return render(request,'blog/blog.html',{'blogs':Blogs})

def detail(request,blog_id):
    return render(request,'blog/detail.html',{'id':blog_id})