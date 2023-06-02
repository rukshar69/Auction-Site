
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

 #Making a custom user model so that we can login using email
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

