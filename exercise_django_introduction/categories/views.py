from django.shortcuts import render

from categories.models import Category
from notes.models import Note


def categories(request):
    all_categories = Category.objects.all()
    categories_with_notes_count = {}
    for category in all_categories:
        notes_count = Note.objects.filter(category=category).count()
        categories_with_notes_count[category] = notes_count
    context = {'all_categories': all_categories, 'categories_with_notes_count': categories_with_notes_count}

    return render(request, 'categories/index.html', context)