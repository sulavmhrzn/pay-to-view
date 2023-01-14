from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.posts_list, name="posts_list"),
    path("tag/<slug:tag>/", views.posts_list, name="posts_list_tag"),
    path("post/<int:id>/<slug:slug>/", views.post_detail, name="post_detail"),
]
