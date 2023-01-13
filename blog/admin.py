from django.contrib import admin

from .models import Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "author",
        "is_published",
        "is_paid",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ["is_published", "is_paid"]
