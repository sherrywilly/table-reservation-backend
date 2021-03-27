from django.urls import path
from customer import views

urlpatterns = [
    path('orders/', views.OrderList.as_view(), name="orders")
]
