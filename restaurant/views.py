from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, View
from restaurant.models import Category, Item, RestCategory, Restaurant
from restaurant.forms import CategoryForm, ItemForm, RestaurantForm, RestcatForm, CategoryUpdateForm
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponse
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


def restCatDel(request, id):
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
    template_name = 'rest/list.html'
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
    form_class = CategoryUpdateForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('rester', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        print(kwargs)
        return super().form_valid(form)


class CategoryList(ListView):
    model = Category
    template_name = 'cat/list.html'
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


class ItemView(View):
    def get(self, request, category=None):
        if category is not None:
            data = Item.objects.filter(category__iexact=category)
        else:
            data = ''

        context = {
            'data': data
        }
        return render(request, "", context)
        pass

    def post(self, request):
        pass

    def update(self, request):
        pass


# class altestView(View):
#     def get(self, request, *args, **kwargs):
#         slug = kwargs['slug']
#         pk = kwargs['id']

#         try:
#             x = Item.objects.filter(category__shop__slug=slug, category__pk=pk)
#             print(x)
#             print("test1")
#         except:
#             x = Item.objects.all()

#         print(x)
#         context = {
#             "items": x,

#         }
#         return HttpResponse(x)


class CategoryListTest(ListView):
    def get(self, *args, **kwargs):
        print(kwargs)
        data = Category.objects.filter(shop__slug=kwargs['slug'])
        context = {
            "data": data
        }
        return render(self.request, "cat/list.html", context)


class ItemListView(ListView):
    def get(self, *args, **kwargs):
        slug = kwargs['slug']
        try:
            res = Restaurant.objects.get(slug=slug)
            x = Item.objects.filter(category__shop__slug__iexact=slug)
        except:
            res = None
            x = None

        context = {
            'data': x,
            'res': res
        }
        print(res)
        return render(self.request, "", context)
