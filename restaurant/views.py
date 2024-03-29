from core.decorators import auth_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, View
from restaurant.models import Category, Item, RestCategory, Restaurant
from restaurant.forms import CategoryForm, ItemForm, RestaurantForm, RestcatForm
from django.urls import reverse, reverse_lazy
from django.http import *

# Create your views here.

decorator = [auth_user, ]

#! Restaurent category views for web


@method_decorator(decorator, name='dispatch')
class RestCategoryCreate(CreateView):
    model = RestCategory
    form_class = RestcatForm
    template_name = 'form.html'
    success_url = reverse_lazy('restcatlist')

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "Category create"
        return x


@method_decorator(decorator, name='dispatch')
class RestCategoryUpdate(UpdateView):
    model = RestCategory
    form_class = RestcatForm
    template_name = 'form.html'
    success_url = reverse_lazy('restcatlist')

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "Catgeory update"
        return x


@method_decorator(decorator, name='dispatch')
class RestCategoryList(ListView):
    model = RestCategory
    template_name = 'restcat/list.html'
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "category"
        return x


@auth_user
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
@method_decorator(decorator, name='dispatch')
class RestaurantCreate(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'form.html'
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Create Restaurant"
        return context


@method_decorator(decorator, name='dispatch')
class RestaurantUpdate(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'form.html'
    success_url = reverse_lazy('restaurant')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "update Restaurant"
        return context


@method_decorator(decorator, name='dispatch')
class RestaurantList(ListView):
    model = Restaurant
    template_name = 'rest/list.html'
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "Restaurants"
        return x

    def get_queryset(self):
        return super().get_queryset().filter(user__is_staff=True, user__is_active=False)
# ! Food category views


@method_decorator(decorator, name='dispatch')
class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    # success_url = reverse_lazy('cat-list-rest')

    # def get_success_url(self, **kwargs):
    #     print(kwargs)
    #     return reverse_lazy('rester', kwargs={'slug': self.kwargs['slug']})

    def get_success_url(self):
        if self.kwargs.get('slug') is not None:
            return reverse_lazy('rester', kwargs={'slug': self.kwargs['slug']})
        else:
            return reverse_lazy('cat-list-rest')

    def form_valid(self, form, *args, **kwargs):
        if self.kwargs.get('slug') is not None:
            form.instance.shop = Restaurant.objects.get(
                slug__iexact=self.kwargs['slug'])
        else:
            form.instance.shop = self.request.user.restaurant
        return super(CategoryCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "category create"
        return x


@method_decorator(decorator, name='dispatch')
class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'

    def get_success_url(self):
        if self.kwargs.get('slug') is not None:
            return reverse_lazy('rester', kwargs={'slug': self.kwargs['slug']})
        else:
            return reverse_lazy('cat-list-rest')

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "category update"
        return x

    # def form_valid(self, form, *args, **kwargs):
    #     print(kwargs)
    #     return super().form_valid(form)


@method_decorator(decorator, name='dispatch')
class CategoryList(ListView):
    model = Category
    template_name = 'cat/list-rest.html'
    context_object_name = 'data'

    def get_queryset(self):
        _x = super().get_queryset()
        print(_x)
        try:
            _y = _x.filter(shop__user=self.request.user)
        except:
            _y = ""
        # print('_y'+_y)
        return _y

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "Category"
        return x

#! Food items Views


@method_decorator(decorator, name='dispatch')
class ItemCreate(View):
    def get(self, request):

        x = ItemForm(user=request.user)
        return render(request, 'form.html', {'form': x, 'heading': "create items"})

    def post(self, request):

        x = ItemForm(user=request.user, data=request.POST,
                     files=request.FILES)
        if x.is_valid():
            _f = x.save(commit=False)
            _f.created_by = request.user
            _f.save()

        return redirect(reverse_lazy('rest-item-list'))


@method_decorator(decorator, name='dispatch')
class ItemUpdate(View):
    def get(self, request, pk):
        i = Item.objects.get(id=pk)
        x = ItemForm(user=request.user, instance=i)
        return render(request, 'form.html', {'form': x, 'heading': 'item-update'})

    def post(self, request, pk):
        i = Item.objects.get(id=pk)
        x = ItemForm(user=request.user, data=request.POST,
                     files=request.FILES, instance=i)
        if x.is_valid():
            x.save()

        return redirect(reverse_lazy('rest-item-list'))


@method_decorator(decorator, name='dispatch')
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

@method_decorator(decorator, name='dispatch')
class CategoryListTest(ListView):
    def get(self, *args, **kwargs):
        print(kwargs)
        data = Category.objects.filter(
            shop__slug=kwargs['slug'])
        context = {
            "data": data,
            'heading': 'category'
        }
        return render(self.request, "cat/list.html", context)


@method_decorator(decorator, name='dispatch')
class ItemListView(View):
    def get(self, request, *args, **kwargs):
        # cid = self.kwargs.get('cid')
        # try:
        #     obj = Item.objects.filter(
        #         category=cid, category__shop=request.user.restaurant)
        # except:
        #     obj = None
        obj = Item.objects.filter(
            category__shop__user__username=request.user.username)
        context = {
            'data': obj,
            'heading': 'items'
        }
        return render(self.request, "item/list.html", context)


@method_decorator(decorator, name='dispatch')
class PendingRest(ListView):
    model = Restaurant
    template_name = "rest/listpending.html"
    context_object_name = "data"

    def get_queryset(self):
        return Restaurant.objects.filter(user__is_staff=False)

    def get_context_data(self, **kwargs):
        x = super().get_context_data(**kwargs)
        x['heading'] = "Pending Restaurents"
        return x

# to activate the restarent from admin side


@auth_user
def restActivate(request, pk=None):
    if pk is not None:
        try:
            _u = Restaurant.objects.get(id=pk)
            _uobj = _u.user
            _uobj.is_staff = True
            _uobj.save()
            return HttpResponseRedirect(reverse('restaurant'))
        except:
            return Http404()
    else:
        return HttpResponseServerError()

# ! 10 -4-2021  starting


# class FoodCategoryView(View):
#     def get(self,request):
#         return render(request,'foodcat.html')


# class ItemUpdate(View):
#     def get(self, request, *args, **kwargs):
#         pass
