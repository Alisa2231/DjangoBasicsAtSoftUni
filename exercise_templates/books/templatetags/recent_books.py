from django import template

from books.models import Book

register = template.Library()

@register.simple_tag
def recent_books():
    latest_books = Book.objects.order_by('-publishing_date')[:3]
    return latest_books