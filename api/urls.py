from api.customauth import CustomAuthToken
from django.urls import path
from django.urls.conf import include
from .views import LocationApiView, RestApiView, CategoryApiView, RestWithLocation, UserViewset
from api.views import OrderApiView
from rest_framework import routers
from rest_framework.authtoken import views

# from tableReservation import api_root

router = routers.DefaultRouter()
router.register('user', UserViewset)
urlpatterns = [
    path('', include(router.urls)),
    path("rest/", RestApiView.as_view(),),
    path("rest/<int:pk>/", RestApiView.as_view(),),
    path("restwithlocation/<int:pk>/", RestWithLocation.as_view(),),

    path('cate/<int:pk>/', CategoryApiView.as_view()),
    path('orders/', OrderApiView.as_view()),
    path('locations/', LocationApiView.as_view()),
    path('auth/user/', CustomAuthToken.as_view()),
    # path('auth/user/', views.obtain_auth_token),


]
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
