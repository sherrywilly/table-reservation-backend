from django.urls import path
from .views import RestApiView

urlpatterns = [
    path("rest/", RestApiView.as_view(),)
]
