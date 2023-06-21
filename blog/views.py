from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Blogpost
from django.contrib import messages

# Create your views here.

def write_blog(request):
    return render(request , "write_blog.html", )

def add_blog(request):
    if request.method == "POST":
        author = request.user
        title = request.POST.get('title')
        content = request.POST.get("content")
        category = request.POST.get('category')
        blogImage = request.POST.get('blogImg')
        print(request.POST.get("save_draf"))
        if "save_blog" in request.POST:
            is_completed = True
            Blogpost.objects.create(title=title,author= author, category=category,content=content,blogImage=blogImage, is_completed = is_completed)
            messages.success(request, 'Your draft saved successfully')
        elif "save_draft" in request.POST :
            is_completed = False
            Blogpost.objects.create(title=title,author= author, category=category,content=content,blogImage=blogImage,is_completed = is_completed)
            messages.success(request, 'Your blog saved successfully')
        else:
           messages.warning(request, 'Your blog has not saved')
        return redirect('index')
    else:
        messages.warning(request, 'Your blog has not saved')
        return redirect('index')

def view_blog(request):
    posts = Blogpost.objects.filter(is_completed=True)
    context = {"posts": posts}
    return render(request, "view_blog.html",context)

def edit_blog(request,id):
    post = get_object_or_404(Blogpost, id=id)
    if request.method == "POST":
        post.author = request.user
        post.title = request.POST.get('title')
        post.content = request.POST.get("content")
        post.category = request.POST.get('category')
        post.blogImage = request.POST.get('blogImg')
        post.is_completed = True
        # post=Blogpost(title=title,author= author, category=category,content=content,blogImage=blogImage, is_completed = True)
        post.save()
        messages.success(request, 'Your blog posted successfully')
        return redirect('index')
    else:
        messages.warning(request, 'Your blog has not saved')
    context = {'post':post}   
    return render(request, "edit_blog.html",context)

def read_blog(request,id):
    post = get_object_or_404(Blogpost, id=id)
    context = {"post": post}
    return render(request, "read_blog.html", context)
    




