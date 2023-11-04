from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms import formset_factory

from blog.models import Photo, Blog
from blog.forms import PhotoForm, BlogForm, DeleteBlogForm


@login_required
def home(request):
    photos = Photo.objects.all().order_by('-date_created')
    blogs = Blog.objects.all().order_by('-date_created')
    context = {
        'photos':photos,
        'blogs':blogs
    }
    return render(request, 'blog/home.html', context)



@login_required
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


@login_required
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



@login_required
def view_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    context = {
        'blog':blog
    }
    return render(request, 'blog/view_blog.html', context)

@login_required
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    delete_form = DeleteBlogForm()
    edit_form = BlogForm()

    if request.method=="POST":
        if 'edit_blog' in request.POST:
            edit_form = BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():                
                edit_form.save()
                return redirect('home')
            
            if 'delete_blog' in request.POST:
                delete_form = DeleteBlogForm(request.POST)
                if delete_form.is_valid():
                    blog.delete()
                    return redirect('home')


    context = {
        'delete_form':delete_form,
        'edit_form': edit_form
    }
    return render(request, 'blog/edit_blog.html', context)

@login_required
def create_multiple_photos(request):
    PhotoFormSet = formset_factory(PhotoForm, extra=5)

    formset = PhotoFormSet()
    if request.method=="POST":
        formset = PhotoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect('home')
    
    context = {
        'formset':formset,
    }
    return render(request, 'blog/create_multiple_photos.html', context)