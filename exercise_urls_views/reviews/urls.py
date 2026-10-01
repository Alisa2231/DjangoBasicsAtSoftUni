from django.urls import path, include

from reviews.views import index, review_by_pk, reviews_by_author

urlpatterns = [
    path('reviews/', include([
        path('', index, name='reviews-index'),
        path('<int:pk>', review_by_pk, name='review-by-pk'),
        path('author/<str:author_name>/', reviews_by_author, name='reviews-by-author'),
    ])),
]