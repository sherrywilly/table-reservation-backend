from django.db import models
from restaurant.models import Item, Restaurant
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    order_status = models.CharField(max_length = 10)
    guest = models.IntegerField()
    date = models.DateField()
    Time = models.TimeField()
    paymentmethod = models.CharField(max_length=100)

class BookingItem(models.Model):
    order = models.ForeignKey(Booking,on_delete=models.CASCADE)
    food = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()


class Rating(models.Model):
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    rating = models.IntegerField(max_length=1,validators=[MaxValueValidator(5),
        MinValueValidator(0)])
