from django.shortcuts import get_object_or_404

from .models import Post


class Tracker:
    """Track viewed post and add it to session with key `viewed_posts`"""

    def __init__(self, request):
        self.session = request.session
        viewed_posts = self.session.get("viewed_posts")
        if not viewed_posts:
            viewed_posts = self.session["viewed_posts"] = {}
        self.viewed_posts = viewed_posts

    def add(self, post_id):
        """Add post to viewed_posts session"""
        post = get_object_or_404(Post, is_published=True, id=post_id)

        if post.is_paid:
            self.viewed_posts[str(post_id)] = {"viewed": True}

        self.save()

    def save(self):
        """Save the modified session"""
        self.session.modified = True

    def __len__(self):
        """Returns number of post in viewed_posts"""
        return len(self.viewed_posts)

    def clear(self):
        """Clear viewed_posts session"""
        del self.session["viewed_posts"]
