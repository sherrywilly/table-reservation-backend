from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
# Create your models here.
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    adddress = models.TextField()
    phone = models.CharField(max_length=12)
    status = models.BooleanField(default=True)
