from django import forms
from customer.models import Booking


class BookingUpdate(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date','time','order_status']
