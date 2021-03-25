from django import forms
from restaurant.models import Category, Item, RestCategory, Restaurant


class RestcatForm(forms.ModelForm):
    class Meta:
        model = RestCategory
        fields = '__all__'


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=['name']
        

# class CategoryUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields=['name']


class ItemForm(forms.ModelForm):
    class Meta:
        model =Item
        fields = '__all__'