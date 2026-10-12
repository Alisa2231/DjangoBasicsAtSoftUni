

from django.urls import path, include

from books import views

app_name = 'books'
urlpatterns = [
    path('add-book/', views.add_book, name='add-book'),
    path('all-books/', views.all_books, name='all-books'),
    path('<slug:slug>/', include([
        path('', views.book_details, name='book-details'),
        path('edit-book/', views.edit_book, name='edit-book'),
        path('delete-book/', views.delete_book, name='delete-book'),

    ]))
]