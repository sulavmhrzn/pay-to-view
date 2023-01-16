from django.conf import settings

from blog.tracker import Tracker


def remaining_posts(request):
    """
    Returns the number of remaining posts
    after subtracting MAX PAID POSTS and the viewed posts.
    """
    tracker = Tracker(request)
    return {"remaining": settings.MAX_PAID_POSTS - len(tracker)}
