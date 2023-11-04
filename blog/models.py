from django.db import models
from django.conf import settings

class Photo(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )
    image = models.ImageField(
        upload_to='PHOTO'
    )
    caption = models.CharField(
        max_length=128,
        blank=True
    )
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    

    def __str__(self):
        return str(self.date_created)

class Blog(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )
    photo = models.ForeignKey(
        Photo, 
        on_delete=models.SET_NULL,
        related_name='photo',
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=128
    )
    content = models.CharField(
        max_length=5000
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    starred = models.BooleanField(default=False)

    def __str__(self):
        return self.title