import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify

from blog.models import Post, Tag


class Command(BaseCommand):
    help = "Adds sample post"

    def add_arguments(self, parser):
        parser.add_argument("count", nargs="+", type=int)

    def create_tags(self):
        self.stdout.write("Creating tags")
        tags = []
        for i in range(5):
            tags.append(Tag(title=f"Tag {i}", slug=slugify(f"Tag {i}")))
        return Tag.objects.bulk_create(tags)

    def handle(self, *args, **options):
        tags = self.create_tags()
        users = User.objects.all()
        posts = []
        for i in range(options["count"][0]):
            user = random.choice(users)
            posts.append(
                Post(
                    title=f"Post title - {i}",
                    content=f"Post content - {i}",
                    slug=slugify(f"Post title - {i}"),
                    author=user,
                    is_paid=random.choice([True, False]),
                    tag=random.choice(tags),
                )
            )
        Post.objects.bulk_create(posts)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully inserted {options['count']} datas")
        )
