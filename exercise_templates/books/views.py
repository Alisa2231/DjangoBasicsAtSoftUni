from django.shortcuts import render

from books.models import Book
from reviews.models import Review


def index(request):
    context = {'books': Book.objects.all(),
               'reviews': Review.objects.all(),}
    return render(request, 'books/index.html', context)

def list_all_books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books/all_books.html', context)

def book_details(request, book_slug):
    context = {'book': Book.objects.get(slug=book_slug)}
    return render(request, 'books/book_details.html', context)
