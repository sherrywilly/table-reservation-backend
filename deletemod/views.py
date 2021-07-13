from django.shortcuts import redirect, render
from restaurant.models import *

# Create your views here.


def deleteRest(request, pk):
    if request.method == "POST":
        Restaurant.objects.get(id=id).delete()

    return redirect(reverse())


def Catedelete(request, pk):
    if request.method == "POST":
        Category.objects.get(id=id).delete()

    return redirect(reverse())


def RestCatdelete(request, pk):
    if request.method == "POST":
        RestCategory.objects.get(id=id).delete()

    return redirect(reverse())


def ItemDelete(request, pk):
    if request.method == "POST":
        Item.objects.get(id=id).delete()
    return redirect(reverse())
