from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student
import string
import random

'''
For this project, every accessbile Model has a Dynamic Slug with some
random string, to have a look_up field other than id and also have non-unique name or title.
'''


@receiver(pre_save, sender = Student)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = ''.join(random.choices(string.ascii_lowercase+string.digits, k=12))
        instance.slug = slug
@receiver(pre_save, sender = Student)
def user_type(sender, instance, *args, **kwargs):
    if instance.user.is_superuser:
        instance.user_type = 'ADMIN'        