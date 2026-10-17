from django.shortcuts import render, redirect

from reviews.forms import ReviewFormBasic
from reviews.models import Review


def add_review(request):
    form = ReviewFormBasic(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'page-title': 'Add Review', 'form': form}
    return render(request, 'reviews/add-review.html', context)

def list_all_reviews(request):
    all_reviews = Review.objects.all()
    context = {'all_reviews': all_reviews,
               'page_title': 'All Reviews',}
    return render(request, 'reviews/all_reviews.html', context)

def review_details(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {'review': review,
               'page_title': f'Review {review_id}',}
    return render(request, 'reviews/review_details.html', context)