from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from destinations.models import Destination
from reviews.models import Review


def index(request: HttpRequest) -> HttpResponse:
    context = {'destinations': Destination.objects.all()}
    return render(request, 'destinations/destinations_template.html', context)

def redirect_view(request: HttpRequest) -> HttpResponse:
    return redirect('destinations-index')

def destination_by_slug(request: HttpRequest, slug: str) -> HttpResponse:
    destination = Destination.objects.get(slug=slug)
    if destination:
        context = {'destination': destination}
        return render(request, 'destinations/destination_by_slug_template.html', context)
    return HttpResponseNotFound()

def destination_by_slug_and_review_by_year(request: HttpRequest, slug: str, year: int) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)
    reviews = get_list_or_404(Review, destination_id=destination.id, created_at__year=year)
    context = {'destination': destination, 'reviews': reviews, 'year': year}
    return render(request, 'destinations/destination_by_slug_and_review_by_year.html', context)

