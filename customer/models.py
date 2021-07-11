import uuid
from django.db import models
from restaurant.models import Item, Restaurant, Category
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.


class Booking(models.Model):
    ORDER_STATUS = (('Pending', 'Pending'), ('Confirmed', 'Confirmed'),
                    ('Completed', 'Completed'), ('Cancelled', 'Cancelled'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    order_status = models.CharField(
        max_length=10, choices=ORDER_STATUS, default='Pending')
    guest = models.IntegerField(validators=[MinValueValidator(1), ])
    date = models.DateField()
    time = models.TimeField()
    paymentmethod = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def total_amount(self):
        _y = []
        _x = self.order_items.all()
        _y = [i.food.price*i.quantity for i in _x]
        return sum(_y)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("order-detail", kwargs={"pk": self.pk})

    def update_url(self):
        return reverse('order-update', kwargs={'pk': self.pk})


class BookingItem(models.Model):
    order = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='order_items')
    food = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        return self.food.name

    def total(self):
        return self.food.price*self.quantity


class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rating = models.IntegerField(validators=[MaxValueValidator(5),
                                             MinValueValidator(0)])
