from django.contrib.auth import logout
from django.shortcuts import redirect, render
from restaurant.models import *

# Create your views here.


def deleteRest(request, pk):
    if request.method == "POST":
        Restaurant.objects.get(id=id).delete()

    return redirect(reverse('restaurant'))


def Catedelete(request, pk):
    if request.method == "POST":
        Category.objects.get(id=id).delete()

    return redirect(reverse("cat-list-rest"))


def RestCatdelete(request, pk):
    if request.method == "POST":
        RestCategory.objects.get(id=id).delete()

    return redirect(reverse('restcatlist'))


def ItemDelete(request, pk):
    if request.method == "POST":
        Item.objects.get(id=id).delete()
    return redirect(reverse("rest-item-list"))


def logout_view(request):
    logout(request)
    return redirect(reverse('login-view'))
