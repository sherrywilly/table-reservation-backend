from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView
from customer.models import Booking, BookingItem, Rating
from django.http import *
from django.urls import reverse, reverse_lazy
from customer.forms import BookingUpdate
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from customer.forms import UserForm, RestUserForm
from restaurant.models import *
from django.utils.decorators import method_decorator
# Create your views here.

decorator = [login_required, ]
#! booking views


@method_decorator(decorator, name='dispatch')
class OrderList(View):
    def get(self, request):
        if not request.user.is_superuser and request.user.is_staff:
            data = Booking.objects.filter(restaurant__user=request.user)

            context = {
                "data": data,
                "heading": 'All orders'
            }
            return render(request, "booking/complist.html", context)

        else:
            data = Booking.objects.all()

            context = {
                "data": data,
                "heading": 'All orders'
            }

            return render(request, "booking/complist.html", context)


@method_decorator(decorator, name='dispatch')
class OrderDetailView(DetailView):
    model = Booking
    template_name = "booking/detail.html"

    def get_object(self):
        _pk = self.kwargs.get('pk')
        print(_pk)
        return get_object_or_404(Booking, id=_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        print(pk)

        return context


@method_decorator(decorator, name='dispatch')
class OrderUpdate(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            booking_object = get_object_or_404(Booking, id=pk)
        except ValidationError as e:
            print(e)
            return HttpResponseRedirect(reverse('orders'))

        x = BookingUpdate(instance=booking_object)

        context = {
            "form": x,
            "heading": "Order Update"
        }
        return render(request, "form.html", context)

    def post(self, request, *args, **kwargs):
        b_obj = Booking.objects.get(id=kwargs.get('pk'))
        form = BookingUpdate(request.POST, instance=b_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('order-update', kwargs={"pk": kwargs.get('pk')}))


@method_decorator(decorator, name='dispatch')
class ChangePass(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        context = {
            "form": form,
            'heading': "change password"
        }
        return render(request, "form.html", context)

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pass-change'))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse('pass-change'))


@method_decorator(decorator, name='dispatch')
class ProfileView(View):
    def get(self, request):
        try:
            if request.user.is_superuser:
                context = {
                    "form": UserForm(instance=request.user)
                }
                return render(request, "profile/detail.html", context)
            else:
                context = {
                    "form": RestUserForm(instance=request.user.restaurant)
                }
                return render(request, "profile/detail.html", context)
        except:
            return render(request, "profile/detail.html")

    def post(self, request):
        try:
            if request.user.is_superuser:
                form = UserForm(data=request.POST, instance=request.user)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('user-profile'))
                else:
                    print(form.errors)
                    raise NameError
            else:
                form = RestUserForm(data=request.POST,
                                    instance=request.user.restaurant)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('user-profile'))
                else:
                    print(form.errors)
                    return HttpResponse(form.errors)

        except:
            return HttpResponseBadRequest("some thing went wrong")


@login_required(login_url='login-view')
def restCatList(request):
    try:
        _x = Category.objects.filter(shop__user=request.user)
    except:
        return Http404("you are not autherised to visit this page")
    context = {
        'data': _x,
        'heading': 'categories'
    }
    return render(request, 'rest-cat-list.html', context)


@login_required(login_url='login-view')
def PendingOrders(request):
    if not request.user.is_superuser and request.user.is_staff:
        data = Booking.objects.filter(
            restaurant__user=request.user, order_status='Pending')

        context = {
            "data": data,
            "heading": "pending Orders"
        }
        return render(request, "booking/list.html", context)

    else:
        data = Booking.objects.filter(order_status='Pending')
        context = {
            "data": data,
            "heading": "pending Orders"

        }
        return render(request, "booking/list.html", context)


@login_required(login_url='login-view')
def CompletedOrders(request):
    if not request.user.is_superuser and request.user.is_staff:
        data = Booking.objects.filter(
            restaurant__user=request.user, order_status__iexact='completed')

        context = {
            "data": data,
            "heading": "Completed Orders"
        }
        return render(request, "booking/complist.html", context)

    else:
        data = Booking.objects.filter(order_status__iexact='completed')
        context = {
            "data": data,
            "heading": "Complete Orders"
        }
        return render(request, "booking/complist.html", context)


@login_required(login_url='login-view')
def ConfirmedOrders(request):
    if not request.user.is_superuser and request.user.is_staff:
        data = Booking.objects.filter(
            restaurant__user=request.user, order_status__iexact='Confirmed')

        context = {
            "data": data,
            "heading": "Confirmed Orders"
        }
        return render(request, "booking/list.html", context)

    else:
        data = Booking.objects.filter(order_status__iexact="Confirmed")
        context = {
            "data": data,
            "heading": "Confirmed Orders"
        }
        return render(request, "booking/list.html", context)


# #############################! order view need to create ##################################


# def Order(request, pk):
#     try:
#         _x = Order.objects.get(id=pk)
#     except:
#         _x = None
#     context = {
#         'data': _x
#     }
#     return
