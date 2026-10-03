from django.urls import path

from books.views import index, list_all_books, book_details

urlpatterns = [
  path('', index, name='landing_page'),
  path('all_books/', list_all_books, name='all_books'),
  path('<slug:book_slug>/', book_details, name='book_details'),

 ]