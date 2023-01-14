import functools

from django.shortcuts import redirect


def anonymous_user_required(fn):
    """
    Decorator for views that checks that the user is not logged in, redirecting
    to the dashboard page.
    """

    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("account:dashboard")
        return fn(request)

    return inner
