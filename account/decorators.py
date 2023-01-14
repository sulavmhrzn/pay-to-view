import functools

from django.shortcuts import redirect


def anonymous_user_required(fn):
    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("account:dashboard")
        return fn(request)

    return inner
