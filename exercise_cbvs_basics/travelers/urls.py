from django.urls import path

from travelers import views

urlpatterns = [
    path('add-traveler/', views.AddTraveler.as_view(), name='add-traveler'),
    path('<int:pk>/edit-traveler/', views.EditTraveler.as_view(), name='edit-traveler'),
    path('<int:pk>/delete-traveler/', views.DeleteTraveler.as_view(), name='delete-traveler'),
]