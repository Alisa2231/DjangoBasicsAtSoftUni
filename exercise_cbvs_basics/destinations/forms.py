from django import forms

from destinations.models import Destination


class DestinationsForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'