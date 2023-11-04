from django.urls import path

from auth_apps import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile-photo/upload/', views.upload_profile_photo, name='upload_profile_photo'),
]
