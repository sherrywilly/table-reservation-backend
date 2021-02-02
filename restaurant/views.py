from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,View
from restaurant.models import Category, Item, RestCategory, Restaurant
from restaurant.forms import CategoryForm, ItemForm, RestaurantForm, RestcatForm
from django.urls import reverse, reverse_lazy
from django.http import Http404
# Create your views here.


#! Restaurent category views for web
class RestCategoryCreate(CreateView):
    model = RestCategory
    form_class = RestcatForm
    template_name = 'form.html'
    success_url = reverse_lazy('restcategory')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RestCategoryUpdate(UpdateView):
    model = RestCategory
    form_class = RestcatForm
    template_name = 'form.html'
    success_url = reverse_lazy('restcatlist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RestCategoryList(ListView):
    model = RestCategory
    template_name = 'restcat/list.html'
    context_object_name = "data"


def restCatDel(request,id):
    if request.method == "POST":
        if id is not None:
            _x = RestCategory.objects.get(id=id)
            _x.delete()
            return reverse('restcatlist')
        else:
            raise Http404("invalid access")
    else:
        raise Http404("invalid request")
   


    

# ! Restaurent views
class RestaurantCreate(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'form.html' 
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RestaurantUpdate(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RestaurantList(ListView):
    model = Restaurant
    template_name = 'form.html'
    context_object_name = "data"


# ! Food category views

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryList(ListView):
    model = Category
    template_name = ''
    context_object_name = 'data'


#! Food items Views

class ItemCreate(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ItemList(ListView):
    model = Item
    template_name = ''
    context_object_name = 'data'