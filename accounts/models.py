from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    # Add more custom fields if needed

    # Add related_name attributes to resolve clashes
    groups = models.ManyToManyField('auth.Group', related_name='custom_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users')



