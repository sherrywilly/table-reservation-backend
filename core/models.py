from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    adddress = models.TextField()
    phone = models.CharField(max_length=12)
    status = models.BooleanField(default=True)

