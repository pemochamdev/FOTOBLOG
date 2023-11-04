from PIL import Image

from django.db import models
from django.conf import settings

class Photo(models.Model):
    IMAGE_MAX_SIZE = (800,800)
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
    
    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        image.save(self.image.path)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

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
    word_count = models.IntegerField(null=True)
    starred = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

    def _get_word_count(self):
        return len(self.content.split(' '))
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.word_count = self._get_word_count()