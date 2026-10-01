from django.urls import path, include

from destinations.views import index, destination_by_slug, destination_by_slug_and_review_by_year

urlpatterns = [
    path('destinations/', include([
        path('', index, name='destinations-index'),
        path('<slug:slug>', destination_by_slug, name='destinations-by-slug'),
        path('<slug:slug>/<int:year>', destination_by_slug_and_review_by_year, name='destination-by-slug-and-review-by-year'),
    ])),
]