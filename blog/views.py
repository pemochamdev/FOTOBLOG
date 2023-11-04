from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from blog.models import Photo, Blog
from blog.forms import PhotoForm, BlogForm

@login_required
def home(request):
    photos = Photo.objects.all().order_by('-date_created')
    blogs = Blog.objects.all().order_by('-date_created')
    context = {
        'photos':photos,
        'blogs':blogs
    }
    return render(request, 'blog/home.html', context)



def photo_upload(request):

    if request.method =='POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)

            photo.uploader = request.user
            photo.date_created = timezone.now()
            photo.save()
            return redirect('home')
    else:
        form = PhotoForm()
    context = {
        'form':form,
    }
    return render(request, 'blog/photo_upload.html', context=context)


def blog_and_photo_upload(request):
    blog_form = BlogForm()
    photo_form = PhotoForm()

    if request.method=="POST":
        blog_form = BlogForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)

        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.date_created = timezone.now()
            photo.save()
    
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.date_created = timezone.now()
            blog.photo = photo
            blog.save()            
            return redirect('home')
    context = {
        'blog_form':blog_form,
        'photo_form':photo_form
    }

    return render(request, 'blog/create_blog_post.html', context)



def view_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    context = {
        'blog':blog
    }
    return render(request, 'blog/view_blog.html', context)