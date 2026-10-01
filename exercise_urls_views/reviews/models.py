from django.db import models

from destinations.models import Destination
from exercise_urls_views.models import TimestampMixin


class Review(TimestampMixin):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    is_published = models.BooleanField(default=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.title