from django.db.models.query_utils import Q
from restaurant.models import Restaurant
from django.contrib.auth.models import User
from django.shortcuts import render
from customer.models import Booking
import datetime

# Create your views here.


def DashBoard(request):
    if request.user.is_superuser:
        users = User.objects.filter(
            is_staff=False, is_superuser=False)
        rest = Restaurant.objects.filter(user__is_active=True)
        orders = Booking.objects.all()
        c_order = orders.filter(order_status__iexact='Completed')
        todays_order = orders.filter(
            ~Q(order_status__iexact='Completed') and Q(date=datetime.date.today())).exclude(order_status__in=['Completed', 'Cancelled'])

        context = {
            'user_count': users.count,
            'rest_count': rest.count,
            'total_order': orders.count,
            'comp_order': c_order.count,
            'todays_order': todays_order,
        }
    else:
        orders = Booking.objects.filter(restaurant__user=request.user)
        pending = orders.filter(order_status__iexact='pending')
        completed = orders.filter(order_status__iexact='completed')
        todays_order = orders.filter(
            ~Q(order_status__iexact='Completed') and Q(date=datetime.date.today())).exclude(order_status__in=['Completed', 'Cancelled']).filter(restaurant__user=request.user)
        print(todays_order)
        context = {
            'total_order': orders.count,
            'pending_orders': pending.count,
            'comp_order': completed.count,
            'todays_order': todays_order
        }
    return render(request, "dashboard.html", context)
