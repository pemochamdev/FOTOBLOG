from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES =(
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    profile_photo = models.ImageField(upload_to='profile')
    
