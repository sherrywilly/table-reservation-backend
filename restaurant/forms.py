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
        fields = ['name']


# class CategoryUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields=['name']


class ItemForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(
            shop__user__username=user.username)

    class Meta:
        model = Item
        exclude = ['created_by']
