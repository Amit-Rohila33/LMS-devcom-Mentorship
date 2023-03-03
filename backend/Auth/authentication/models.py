# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, name='email')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(default='STUDENT', max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length = 255,blank=False, name='name')
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='user/images/', default='', blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email