from django.urls import path
from restaurant.views import CategoryCreate, CategoryList, CategoryUpdate, RestCategoryCreate, RestCategoryList, RestCategoryUpdate, RestaurantCreate, RestaurantList, RestaurantUpdate

urlpatterns = [
    # !create path in restaurent module
    # path('category/',RestCategoryCreate.as_view(),name="restcategory"),
    # path('restaurant/',RestaurantCreate.as_view(),name="restaurant"),
    # path('restaurant/category/',CategoryCreate.as_view(),name="restaurant"),
    #!update paths in restaurant modules
    path('category/<int:pk>',RestCategoryUpdate.as_view(),name='restcatupdate'),
    path('restaurant/<int:pk>',RestaurantUpdate.as_view(),name="restaurant"),
    path('restaurant/category/<int:pk>',CategoryUpdate.as_view(),name="restaurant"),
    #!list view paths in restaurant module
    path('category/',RestCategoryList.as_view(),name="restcatlist"),
    path('restaurant/',RestaurantList.as_view(),name="restaurant"),
    path('restaurant/category/',CategoryList.as_view(),name="restaurList")
]