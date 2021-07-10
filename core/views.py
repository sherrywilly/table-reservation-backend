from django.db.models.query_utils import Q
from restaurant.models import Restaurant
from django.contrib.auth.models import User
from django.shortcuts import render
from customer.models import Booking
import datetime
# Create your views here.


def DashBoard(request):
    users = User.objects.filter(
        is_staff=False, is_superuser=False)
    rest = Restaurant.objects.filter(user__is_active=True)
    orders = Booking.objects.all()
    c_order = orders.filter(order_status__iexact='Completed')
    todays_order = orders.filter(
        ~Q(order_status__iexact='Completed') and Q(date=datetime.date.today()))

    print(todays_order)
    context = {
        'user_count': users.count,
        'rest_count': rest.count,
        'total_order': orders.count,
        'comp_order': c_order.count,
    }
    return render(request, "dashboard.html", context)
