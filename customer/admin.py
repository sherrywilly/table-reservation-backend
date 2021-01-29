from django.contrib import admin
from .models import Booking
from customer.models import BookingItem, Rating

# Register your models here.
admin.site.register(Booking)
admin.site.register(BookingItem)
admin.site.register(Rating)
