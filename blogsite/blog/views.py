from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.http import HttpResponse
from .form import BlogForm

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request,"blog/index.html",{"blogs": blogs})

def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request,"blog/detail.html", {"blog": blog})

def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect(blog_list)
    else:
        form = BlogForm(instance=blog)
    return render(request, "blog/edit.html",{'form':form})

def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog/delete.html',{'blog': blog})

def home(request):
    return HttpResponse("Hi there")