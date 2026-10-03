from django.shortcuts import render

from books.models import Book
from reviews.models import Review


def index(request):
    context = {'books': Book.objects.all(),
               'reviews': Review.objects.all(),
               'page_title': 'Books with reviews'}
    return render(request, 'books/index.html', context)

def list_all_books(request):
    context = {'books': Book.objects.all(),
               'page_title': 'All Books'}
    return render(request, 'books/all_books.html', context)

def book_details(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    context = {'book': book,
               'page_title': f'{book.title} by {book.author}'}
    return render(request, 'books/book_details.html', context)
