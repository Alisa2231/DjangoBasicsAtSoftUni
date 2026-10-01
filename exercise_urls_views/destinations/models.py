from django.db import models
from django.utils.text import slugify

from exercise_urls_views.models import TimestampMixin


class Destination(TimestampMixin):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True, blank=True)
    description = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)




