from django.db import models

from books.models import Book


class Review(models.Model):
    class ReviewType(models.TextChoices):
        TEXT = 'txt', 'Text'
        VIDEO = 'video', 'Video'
        AUDIO = 'audio', 'Audio'

    author = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    review_type = models.CharField(max_length=5, choices=ReviewType)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)