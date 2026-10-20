from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from travelers.models import Traveler


class AddTraveler(CreateView):
    model = Traveler
    fields = '__all__'
    template_name = 'travelers/add-traveler.html'
    success_url = reverse_lazy('common:home')

class EditTraveler(UpdateView):
    model = Traveler
    fields = '__all__'
    template_name = 'travelers/edit-traveler.html'
    success_url = reverse_lazy('common:home')

class DeleteTraveler(DeleteView):
    model = Traveler
    template_name = 'travelers/delete-traveler.html'
    success_url = reverse_lazy('common:home')
