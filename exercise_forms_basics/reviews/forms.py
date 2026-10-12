from django import forms
from reviews.models import Review


# class ReviewFormBasic(forms.Form):
#     REVIEW_TYPE = (
#         ('txt', 'Text'),
#         ('video', 'Video'),
#         ('audio', 'Audio'),
#     )
#
#     author = forms.CharField(max_length=100, label='Author', help_text="Your full name please")
#     body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your review here'}), label='Review content')
#     rating = forms.DecimalField(max_digits=4, decimal_places=2, label='Rating', help_text="Between 0.00 and 5.00")
#     is_verified = forms.BooleanField(required=False, initial=False)
#     review_type = forms.ChoiceField(choices=REVIEW_TYPE)
#     book = forms.ModelChoiceField(queryset=Book.objects.all())

class ReviewFormBasic(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'