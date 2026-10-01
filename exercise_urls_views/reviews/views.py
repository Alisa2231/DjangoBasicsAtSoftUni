from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from destinations.models import Destination
from reviews.models import Review


def index(request):
    context = {'recent_reviews': Review.objects.order_by('-created_at')[:5]}
    return render(request, 'reviews/reviews-template.html', context)

def review_by_pk(request, pk):
    review = get_object_or_404(Review, id=pk)
    destination = Destination.objects.get(id=review.destination_id)
    context = {'review': review, 'destination': destination}
    return render(request, 'reviews/reviews-by-pk-template.html', context)

def reviews_by_author(request, author_name: str):
    reviews = Review.objects.filter(author=author_name).order_by('-created_at')
    if reviews:
        context = {'reviews': reviews, 'author': author_name}
        return render(request, 'reviews/reviews-by-author-template.html', context)
    return HttpResponse(status=404)
