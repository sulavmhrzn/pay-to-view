from django.shortcuts import get_object_or_404, render

from .models import Post, Tag


def posts_list(request, tag=None):
    posts = Post.published_manager.all()
    tags = Tag.objects.all()
    if tag:
        posts = posts.filter(tag__slug=tag)
    return render(
        request, "blog/list.html", context={"posts": posts, "tags": tags, "tag": tag}
    )


def post_detail(request, slug=None, id=None):
    post = get_object_or_404(Post, is_published=True, slug=slug, id=id)
    return render(request, "blog/detail.html", context={"post": post})
