from core.views import DashBoard, create_loc, deleteLoc, location_list, login_page, registration, update_loc
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# import debug_toolbar
from django.contrib.auth import update_session_auth_hash, views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('', include('customer.urls')),
    path('api/', include('api.urls')),
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ! password reset


    path('password-reset/',
         auth_views.PasswordResetView.as_view(

             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
         ),
         name='password_reset_complete'),
    path('', login_page, name="login-view"),
    path('register/', registration, name="register-view"),
    path('dashboard/', DashBoard, name="dashboard"),
    path('locations/', location_list, name="location-list"),
    path('locations/create/', create_loc, name="loc-create"),
    path('locations/<int:pk>/update/', update_loc, name="locupdate"),
    path('locations/<int:pk>/delete/', deleteLoc, name="locdelete"),
    path('', include('deletemod.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
