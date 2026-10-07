from django.urls import path, include
from petstagram.photos import views

app_name = 'photos'
urlpatterns = [
    path('add/', views.photo_add_view, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_view, name='photo-details'),
        path('edit/', views.photo_edit_view, name='photo-edit'),
    ]))
]