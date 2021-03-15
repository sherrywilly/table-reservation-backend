from django.urls import path
from .views import RestApiView, CategoryApiView

urlpatterns = [
    path("rest/", RestApiView.as_view(),),
    path('cate/', CategoryApiView.as_view())
]
