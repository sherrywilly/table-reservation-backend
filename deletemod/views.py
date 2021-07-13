from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from restaurant.models import *

# Create your views here.


@login_required(login_url='login-view')
def deleteRest(request, pk):
    if request.method == "POST":
        Restaurant.objects.get(id=pk).delete()

    return redirect(reverse('restaurant'))


@login_required(login_url='login-view')
def Catedelete(request, pk):
    if request.method == "POST":
        Category.objects.get(id=pk).delete()

    return redirect(reverse("cat-list-rest"))


@login_required(login_url='login-view')
def RestCatdelete(request, pk):
    if request.method == "POST":
        RestCategory.objects.get(id=pk).delete()

    return redirect(reverse('restcatlist'))


@login_required(login_url='login-view')
def ItemDelete(request, pk):
    if request.method == "POST":
        Item.objects.get(id=pk).delete()
    return redirect(reverse("rest-item-list"))


def logout_view(request):
    logout(request)
    return redirect(reverse('login-view'))
