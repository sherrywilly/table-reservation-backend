from django.shortcuts import redirect
from django.urls.base import reverse


def unauth_user(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('dashboard'))

    return wrapper
