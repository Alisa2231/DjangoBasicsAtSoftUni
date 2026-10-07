from django.shortcuts import render

def photo_add_view(request):
    return render(request, 'photos/photo-add-page.html')

def photo_details_view(request):
    return render(request, 'photos/photo-detils-page.html')

def photo_edit_view(request):
    return render(request, 'photos/photo-edit-page.html')
