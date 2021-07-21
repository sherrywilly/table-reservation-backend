from core.decorators import auth_user
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from restaurant.models import *

# Create your views here.


@auth_user
def deleteRest(request, pk):
    if request.method == "POST":
        Restaurant.objects.get(id=pk).delete()

    return redirect(reverse('restaurant'))


@auth_user
def Catedelete(request, pk):
    if request.method == "POST":
        Category.objects.get(id=pk).delete()

    return redirect(reverse("cat-list-rest"))


@auth_user
def RestCatdelete(request, pk):
    if request.method == "POST":
        RestCategory.objects.get(id=pk).delete()

    return redirect(reverse('restcatlist'))


@auth_user
def ItemDelete(request, pk):
    if request.method == "POST":
        Item.objects.get(id=pk).delete()
    return redirect(reverse("rest-item-list"))


def logout_view(request):
    logout(request)
    return redirect(reverse('login-view'))


@auth_user
def UserDelete(request, pk):
    if request.method == "POST":
        User.objects.get(id=pk).delete()
    return redirect(reverse("user-list"))


@auth_user
def users_view(request):
    users = User.objects.filter(is_active=True).exclude(
        is_superuser=True, is_staff=True).filter(restaurant__isnull=True)
    context = {'data': users,
               'heading': "users"
               }
    return render(request, "user/list.html", context)
