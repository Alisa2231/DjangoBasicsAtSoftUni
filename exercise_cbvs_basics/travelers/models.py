from django.core.validators import MinValueValidator
from django.db import models

from common.choices import Countries
from travelers import validators


class Traveler(models.Model):

    class GENDERS(models.TextChoices):
        M = "M", "Male"
        F = "F", "Female"
        OTHER = "OTHER", "Other"

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[validators.domain_validator])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
    country = models.CharField(max_length=100, choices=Countries)
    gender = models.CharField(max_length=100, choices=GENDERS)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

