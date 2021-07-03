from django.urls import path
from .views import LocationApiView, RestApiView, CategoryApiView
from api.views import OrderApiView
# from tableReservation import api_root

urlpatterns = [
    path("rest/", RestApiView.as_view(),),
    path("rest/<int:pk>/", RestApiView.as_view(),),

    path('cate/<int:pk>/', CategoryApiView.as_view()),
    path('orders/', OrderApiView.as_view()),
    path('locations/', LocationApiView.as_view())

]
