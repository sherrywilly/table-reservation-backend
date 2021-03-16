from django.urls import path
from .views import RestApiView, CategoryApiView
# from tableReservation import api_root

urlpatterns = [
    path("rest/", RestApiView.as_view(),),
    path("rest/<int:pk>/", RestApiView.as_view(),),

    path('cate/', CategoryApiView.as_view())
]
