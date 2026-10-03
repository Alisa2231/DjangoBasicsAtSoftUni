from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    class GENRES(models.TextChoices):
        FICTION = 'FICTION', 'Fiction'
        NON_FICTION = 'NON_FICTION', 'Non-Fiction'
        FANTASY = 'FANTASY', 'Fantasy'
        SCIENCE = 'SCIENCE', 'Science'
        BIOGRAPHY = 'BIOGRAPHY', 'Biography'
        CRIME = 'CRIME', 'Crime'
        MYSTERY = 'MYSTERY', 'Mystery'
        THRILLER = 'THRILLER', 'Thriller'
        ROMANCE = 'ROMANCE', 'Romance'
        HISTORY = 'HISTORY', 'History'
        HORROR = 'HORROR', 'Horror'

    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100, choices=GENRES.choices)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.CharField(editable=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title} by {self.author}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
