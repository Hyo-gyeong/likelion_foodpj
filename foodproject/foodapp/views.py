
from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Blog 

def foodlist(request):
    blog = Blog.objects.all()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    
    try: 
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = page.get_page(1)
    except EmptyPage :
        posts = paginator.get_page(paginator.num_pages)

    return render(request, 'foodlist.html', {'blog' : blog, 'posts' : posts})

def new (request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.description = request.POST['description']
    if request.method == 'POST'and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        blog.image = fs.url(filename)
    blog.save()
    return redirect('/')
   

def detail(request, blog_id):
    blog = Blog.objects.get(pk = blog_id) # pk에 조건 여러가지 걸수 있음 #

    return render(request, 'detail.html', {'blog': blog})

def edit(request, blog_id):

    blog = get_object_or_404(Blog, pk = blog_id )
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.description = request.POST['description']
        if request.FILES['image']:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            blog.image = fs.url(filename)
        blog.save()

        return redirect('/')
    else:
        return render(request, 'edit.html', {'blog' : blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()

    return redirect('/')
    