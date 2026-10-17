from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('add-review', views.add_review, name='add-review'),
    path('all_reviews/', views.list_all_reviews, name='all-reviews'),
    path('<int:review_id>/', views.review_details, name='review-details'),
]