from django.db.models import fields
from django.forms import widgets
from django.template.defaultfilters import first
from restaurant.models import *
from django import forms
from django.contrib.auth.models import User


class RestaurantRegisterForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['name',
                  'phone', 'categorys', 'location', 'logo', 'opentime', 'closstime']
        widgets = {
            'opentime': forms.TimeInput(attrs={'type': 'time'}),
            'closstime': forms.TimeInput(attrs={'type': 'time'})
        }


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
