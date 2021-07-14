from django.shortcuts import redirect
from django.urls.base import reverse


def unauth_user(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('dashboard'))

    return wrapper


def auth_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user is not None:
            print(request.user)
            if request.user.is_staff or request.user.is_staff:

                return view_func(request, *args, **kwargs)
            else:
                return redirect(reverse('logout-view'))
        else:
            return redirect(reverse('login-view'))

    return wrapper
