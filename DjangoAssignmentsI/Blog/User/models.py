from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False, null=False)
    profile_img = models.ImageField(default='default-img.png', blank=True, null=True)
