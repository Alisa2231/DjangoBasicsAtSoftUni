from django.shortcuts import render

from reviews.models import Review


def recent_reviews(request):
    latest_reviews = Review.objects.order_by('-created_at')[:5]
    context = {'recent_reviews': latest_reviews}
    return render(request, 'reviews/recent_reviews.html', context)

def review_details(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {'review': review}
    return render(request, 'reviews/review_details.html', context)