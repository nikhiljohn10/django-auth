from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username