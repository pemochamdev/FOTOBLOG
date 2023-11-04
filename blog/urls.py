from django.urls import path

from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photo/upload/', views.photo_upload, name='photo_upload'),
    path('blog/create', views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:id>', views.view_blog, name='view_blog'),

]
