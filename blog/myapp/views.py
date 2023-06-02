from django.shortcuts import render
from myapp.models import Blog
def home_view(request):
    blogs = Blog.objects.all()
    print(blogs)
    context = {
        "Blog": blogs,
    }
    return render(request, 'home.html', context)
def newpost_view(request):
    return render(request,'newpost.html',{})

def addpost_view(request):
    title=request.POST.get("title")
    print(title)
    desc = request.POST.get("desc")
    print(desc)
    blog=Blog(title=title,desc=desc)
    blog.save()
    return render(request, 'newpost.html', {})
def delete_project(request, pk):
    print("In delete")
    Blog.objects.filter(pk=pk).delete()

    blogs = Blog.objects.all()
    print(blogs)
    context = {
        'Blog': blogs
    }
    return render(request, 'home.html', context)