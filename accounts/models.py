from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

def user_directory_path(instance, filename):
    return 'profile/{0}_{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    bio = models.TextField(blank=True, max_length=500)
    email_verified = models.BooleanField(default=False)
    picture = models.ImageField(upload_to=user_directory_path)
    dob = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
