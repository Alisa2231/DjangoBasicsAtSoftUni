from django.urls import path

from reviews import views

urlpatterns = [
    path('add-review', views.add_review, name='add-review'),
]