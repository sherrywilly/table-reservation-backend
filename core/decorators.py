from django.shortcuts import redirect


def unauth_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            print('authenticated')
            return redirect('dashboard')
        else:
            return redirect('login')
    return wrapper
