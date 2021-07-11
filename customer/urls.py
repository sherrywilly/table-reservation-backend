from django.urls import path
from customer import views

urlpatterns = [
    path('rest-category/', views.restCatList, name="rest-cat-list"),
    path('orders/', views.OrderList.as_view(), name="orders"),
    #!############################### only for restaurents ##################################
    path('orders/pending/', views.PendingOrders, name="orders-pending"),
    path('orders/complete/', views.CompletedOrders, name="orders-completed"),
    path('orders/confirmed/', views.ConfirmedOrders, name="orders-confirmed"),
    #!############################### ends only for restaurents ##################################
    #!############################### for Both restaurents and admin #############################
    path('orders/<pk>/', views.OrderDetailView.as_view(), name="order-detail"),
    path('orders/<pk>/update_order/',
         views.OrderUpdate.as_view(), name="order-update"),
    path('user/changepass/', views.ChangePass.as_view(), name="pass-change"),
    path('user/profile/', views.ProfileView.as_view(), name="user-profile")
]
