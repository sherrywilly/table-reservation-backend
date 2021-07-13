from django.urls import path
from .views import *
urlpatterns = [
    path('restcategory/<int:pk>/delete/', RestCatdelete, name="restcat-delete"),
    path('category/<int:pk>/delete/', Catedelete, name="cat-delete"),
    path('restaurant/<int:pk>/delete/', deleteRest, name="rest-delete"),
    path('item/<int:pk>/delete/', deleteRest, name="item-delete"),
    path('logout/', logout_view, name="logout-view"),
    
]
