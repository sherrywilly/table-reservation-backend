from django.urls import path
from customer import views

urlpatterns = [
    path('rest-category/', views.restCatList, name="rest-cat-list"),
    path('orders/', views.OrderList.as_view(), name="orders"),
    path('orders/<pk>/', views.OrderDetailView.as_view()),
    path('orders/<pk>/update_order/',
         views.OrderUpdate.as_view(), name="order-update"),
    path('user/changepass/', views.ChangePass.as_view(), name="pass-change"),
    path('user/profile/', views.ProfileView.as_view(), name="user-profile")
]
