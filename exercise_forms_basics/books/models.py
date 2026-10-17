from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify


class Book(models.Model):
    class Genre(models.TextChoices):
        FICTION = 'fiction', "Fiction"
        NON_FICTION = 'non-fiction', "Non-Fiction"
        FANTASY = 'fantasy', "Fantasy"
        SCIENCE = 'science', "Science"

    class Language(models.TextChoices):
        ENGLISH = 'en', "English"
        BULGARIAN = 'bg', "Bulgarian"
        FRENCH = 'fr', "French"
        GERMAN = 'de', "German"
        OTHER = 'other', "Other"


    title = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100, choices=Genre)
    language = models.CharField(max_length=100, choices=Language)
    pages = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    cover_image = models.ImageField(upload_to='cover_images', null=True, blank=True)
    sample_chapter = models.FileField(upload_to='sample_chapters', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
