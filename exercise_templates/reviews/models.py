from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from books.models import Book


class Review(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 validators=[
                                     MinValueValidator(Decimal("1.00")),
                                     MaxValueValidator(Decimal("5.00")),
                                 ],
                                 )
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.title
