from django.urls import path
from restaurant.views import CategoryCreate, CategoryList, CategoryUpdate, RestCategoryCreate, RestCategoryList, RestCategoryUpdate, RestaurantCreate, RestaurantList, RestaurantUpdate, CategoryListTest,ItemListView
urlpatterns = [
    # !create path in restaurent module
    path('category/create/', RestCategoryCreate.as_view(),
         name="restcategorycreate"),
    path('restaurant/create/', RestaurantCreate.as_view(), name="restaurantcreate"),
    path('restaurant/category/create/',
         CategoryCreate.as_view(), name="restaurantcatcreate"),

    #!update paths in restaurant modules
    path('category/<int:pk>', RestCategoryUpdate.as_view(), name='restcatupdate'),
    path('restaurant/<int:pk>', RestaurantUpdate.as_view(), name="restaurantupdate"),
    path('<slug:slug>/category/<int:pk>',
         CategoryUpdate.as_view(), name="catupdate"),
    #!list view paths in restaurant module1
    path('category/', RestCategoryList.as_view(), name="restcatlist"),
    path('restaurant/', RestaurantList.as_view(), name="restaurant"),
#     path('restaurant/category/', CategoryList.as_view(), name="restcateList"),
    path('<slug:slug>/category/', CategoryListTest.as_view(), name="rester"),

#     path('<slug:slug>/<int:id>/test/', altestView.as_view(), name="test"),
    
    
    #!feb 14 updating
    path('<slug:slug>/item/',ItemListView.as_view(),name="itemlist"),

]
