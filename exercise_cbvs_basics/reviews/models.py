from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from destinations.models import Destination
from travelers.models import Traveler


class Review(models.Model):
    class ReviewTypes(models.TextChoices):
        TEXT = 'TXT', 'Text'
        AUDIO = 'AUDIO', 'Audio'
        VIDEO = 'VIDEO', 'Video'

    title = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    is_verified = models.BooleanField(default=False)
    review_type = models.CharField(max_length=100, choices=ReviewTypes)
    created_at = models.DateTimeField(auto_now_add=True)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def clean(self):
        if self.destination.id and not self.destination.is_available:
            raise ValidationError('Cannot create a review for an unavailable destination')

    def __str__(self):
        return self.title