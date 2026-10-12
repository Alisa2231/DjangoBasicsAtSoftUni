from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookAddForm, BookEditForm, BookDeleteForm
from .models import Book


def index(request):
    context = {'page-title': 'Book Hub'}
    return render(request, 'base.html', context)

def add_book(request):
    form = BookAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books: all-books')
    context = {'page-title': 'Add Book', 'form': form}
    return render(request, 'books/add-book.html', context)

def all_books(request):
    books = Book.objects.all()
    context = {'books': books,
               'page-title': 'All Books',}
    return render(request, 'books/all-books.html', context)

def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {'book': book,
               'page-title': 'Book Details',}
    return render(request, 'books/book-details.html', context)

def edit_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    form = BookEditForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('books:book-details', slug=book.slug)
    context = {'form': form,}
    return render(request, 'books/edit-book.html', context)

def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    form = BookDeleteForm(request.POST or None, instance=book)
    if request.method == 'POST':
        book.delete()
        return redirect('books:all-books')
    context = {'form': form,}
    return render(request, 'books/delete-form.html', context)