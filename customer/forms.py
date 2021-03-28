from django import forms
from customer.models import Booking
from django.contrib.auth.models import User
from core.models import Profile
from restaurant.models import Restaurant


class BookingUpdate(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'order_status']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']



class RestUserForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude =['user','slug','lat','log']