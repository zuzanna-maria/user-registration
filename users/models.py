from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=500)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    date_of_birth = models.DateField(max_length=500)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
