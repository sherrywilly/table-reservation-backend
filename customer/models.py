from django.db import models
from restaurant.models import Item, Restaurant
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    order_status = models.CharField(max_length = 10)
    guest = models.IntegerField(validators=[MinValueValidator(1),])
    date = models.DateField()
    Time = models.TimeField()
    paymentmethod = models.CharField(max_length=100)

    def __str__(self):
        return self.order_status
    

class BookingItem(models.Model):
    order = models.ForeignKey(Booking,on_delete=models.CASCADE)
    food = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        return self.food

class Rating(models.Model):
    restaurant  = models.ForeignKey(Restaurant,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    rating = models.IntegerField(validators=[MaxValueValidator(5),
        MinValueValidator(0)])

    
