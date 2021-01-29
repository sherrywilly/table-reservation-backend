from django.contrib import admin
from restaurant.models import Category, Item, RestCategory, Restaurant

# Register your models here.
admin.site.register(RestCategory)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Item)