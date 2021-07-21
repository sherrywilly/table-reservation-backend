from django.contrib.auth import login
from django.contrib import messages
from django.contrib.messages.api import error
from django.db.models.query_utils import Q
from restaurant.models import Restaurant
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from customer.models import Booking
import datetime
from core.form import *
from core.decorators import auth_user, unauth_user
from django.contrib.auth.decorators import login_required

# Create your views here.


@auth_user
def DashBoard(request):
    if request.user.is_superuser:
        users = User.objects.filter(is_active=True).exclude(
            is_superuser=True, is_staff=True).filter(restaurant__isnull=True)
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


@unauth_user
def registration(request):
    f1 = RestaurantRegisterForm(request.POST or None, request.FILES or None)
    f2 = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if f1.is_valid() and f2.is_valid():
            password = f2.cleaned_data.get('password')
            user = f2.save(commit=False)
            user.set_password(password)
            user.is_active = True
            x = user.save()
            print(user)
            rest = f1.save(commit=False)
            print(x)
            rest.user = user
            rest.save()
            messages.success(
                "you are successfully registred into the system please wait for admin confirmation")
        else:
            messages.error(request, f2.errors)
            messages.error(request, f1.errors)

    context = {
        'form1': f1,
        'form2': f2
    }
    return render(request, "account/register.html", context)


@unauth_user
def login_page(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('password')
        print(uname, password)
        try:
            user = User.objects.filter(Q(username=uname) | Q(email=uname))[0]
            print(user)
            if user is None:
                raise ValueError
            if user.is_staff or user.is_superuser:
                if user.check_password(password):
                    login(request, user)
                    return redirect(reverse('dashboard'))
                else:
                    messages.error(request, 'InValid Credentials')
            else:
                messages.error(
                    request, 'please wait until we verify your account')
        except Exception as e:
            print(e)
            messages.error(
                request, 'we cant find your account in  this system')

    return render(request, "account/login.html")


@auth_user
def location_list(request):
    x = Location.objects.all()
    context = {
        "data": x,
        "heading": "Location"
    }
    return render(request, 'loclist.html', context)


@auth_user
def create_loc(request):
    form = LocationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse('location-list'))
        else:
            print(form.errors)

    context = {
        'form': form,
        'heading': "create Location"
    }
    return render(request, "form.html", context)


@auth_user
def update_loc(request, pk):
    x = Location.objects.get(id=pk)
    form = LocationForm(request.POST or None, instance=x)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse('location-list'))
        else:
            print(form.errors)

    context = {
        'form': form,
        "heading": "Update Location"
    }
    return render(request, "form.html", context)


@auth_user
def deleteLoc(request, pk):
    if request.method == "POST":
        Location.objects.get(id=pk).delete()
    return redirect(reverse('location-list'))
