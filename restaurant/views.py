from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,View
from restaurant.models import Category, Item, RestCategory, Restaurant
from restaurant.forms import CategoryForm, ItemForm, RestcatForm
from django.urls import reverse_lazy
# Create your views here.


#! Restaurent category views for web
class RestCategoryCreate(CreateView):
    model = RestCategory
    form_class = RestcatForm
    template = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RestCategoryUpdate(UpdateView):
    model = RestCategory
    form_class = RestcatForm
    template = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RestCategoryList(ListView):
    model = RestCategory
    template = 'form.html'
    context_object_name = "data"


# ! Restaurent views
class RestaurantCreate(CreateView):
    model = Restaurant
    form_class = RestcatForm
    template = 'form.html' 
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RestaurantUpdate(UpdateView):
    model = Restaurant
    form_class = RestcatForm
    template = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RestaurantList(ListView):
    model = Restaurant
    template = 'form.html'
    context_object_name = "data"


# ! Food category views

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryList(ListView):
    model = Category
    template = ''
    context_object_name = 'data'


#! Food items Views

class ItemCreate(CreateView):
    model = Item
    form_class = ItemForm
    template = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemForm
    template = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ItemList(ListView):
    model = Item
    template = ''
    context_object_name = 'data'