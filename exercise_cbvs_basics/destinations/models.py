from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from common.choices import Countries
from travelers.models import Traveler


class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, choices=Countries)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    travelers = models.ManyToManyField(Traveler, related_name='destinations')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "country"],
                name="unique_destination"
            )
        ]
