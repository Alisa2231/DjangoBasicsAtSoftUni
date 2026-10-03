from django.urls import path

from reviews.views import recent_reviews, review_details

urlpatterns = [
    path('recent_reviews/', recent_reviews, name='recent_reviews'),
    path('<int:review_id>/', review_details, name='review_details'),
]