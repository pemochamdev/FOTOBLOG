from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.conf import settings

from auth_apps.forms import LoginForm, SignUpForm, UploadProfilePhotoForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
        
            user = authenticate(
                username = form.cleaned_data.get('username'), 
                password = form.cleaned_data.get('password')
            )

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    else:
        form = LoginForm()
        message=''
    context = {
        'form':form,
        'message':message,
    }

    return render(request, 'register/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def signup_view(request):    
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)        
    else:
        form = SignUpForm()
    context = {'form':form,}
    return render(request, 'register/signup.html', context)


def upload_profile_photo(request):
    form = UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'auth_apps/upload_profile_photo.html', context={'form': form})