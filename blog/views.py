from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Post, Tag
from .tracker import Tracker


def posts_list(request, tag=None):
    """View that returns published posts."""
    posts = Post.published_manager.select_related("author").all()
    tags = Tag.objects.all()
    if tag:
        posts = posts.filter(tag__slug=tag)
    return render(
        request, "blog/list.html", context={"posts": posts, "tags": tags, "tag": tag}
    )


def post_detail(request, slug=None, id=None):
    """
    View that returns post details that match the slug and id parameters passed in.
    Checks the session to determine the number of posts viewed.
    If the user does not have a membership and has viewed more than three paid posts,
    the view returns a limit exceeded page.
    """
    post = get_object_or_404(
        Post.objects.select_related("author", "tag"),
        is_published=True,
        slug=slug,
        id=id,
    )
    tracker = Tracker(request)

    # Check if the user is authenticated and has purchased a membership
    if request.user.is_authenticated and request.user.profile.has_membership:
        return render(request, "blog/detail.html", context={"post": post})

    # check if post is paid and length of viewed_posts session is greater than 3
    if post.is_paid and len(tracker) >= settings.MAX_PAID_POSTS:
        return render(request, "blog/limit_exceeded.html")
    tracker.add(post.id)

    return render(request, "blog/detail.html", context={"post": post})
