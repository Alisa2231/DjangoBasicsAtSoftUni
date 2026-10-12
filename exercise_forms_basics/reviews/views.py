from django.shortcuts import render, redirect

from reviews.forms import ReviewFormBasic


def add_review(request):
    form = ReviewFormBasic(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    context = {'page-title': 'Add Review', 'form': form}
    return render(request, 'reviews/add-review.html', context)