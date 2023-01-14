from django.db import models


class Membership(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title
