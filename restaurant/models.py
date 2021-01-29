from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RestCategory(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=12)
    categorys = models.ManyToManyField(RestCategory)
    lat = models.FloatField()
    log = models.FloatField()
    status = models.BooleanField(default=False)
    opentime = models.TimeField()
    closstime = models.TimeField()
    seatingCapacity = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    # logo and pics for the restaurent is needed here


class Category(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey(Restaurant,on_delete=models.CASCADE,blank=True,null=True)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price =models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    # image fierld required
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)