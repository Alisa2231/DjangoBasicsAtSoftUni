from django import forms

from travelers.models import Traveler


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = '__all__'