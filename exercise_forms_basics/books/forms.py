from django import forms
from django.core.exceptions import ValidationError

from books.models import Book
from books.validators import ValidatePrice


# class BookFormBasic(forms.Form):
#     GENRES = (
#         ('Fiction', 'Fiction'),
#         ('non-fiction', "Non-Fiction"),
#         ('fantasy', "Fantasy"),
#         ('science', "Science")
#     )
#
#     LANGUAGES = (
#         ('en', "English"),
#         ('bg', "Bulgarian"),
#         ('fr', "French"),
#         ('de', "German"),
#         ('other', "Other")
#     )
#
#     title = forms.CharField(max_length=100, label='Book Title')
#     price = forms.DecimalField(max_digits=6, decimal_places=2, label='Book Price')
#     isbn = forms.CharField(max_length=13, label='ISBN', help_text="Must be unique")
#     genre = forms.ChoiceField(choices=GENRES, label='Genre', help_text="Select from the drop-down menu")
#     language = forms.ChoiceField(choices=LANGUAGES, label='Language', help_text="Select from the drop-down menu")
#     pages = forms.IntegerField(min_value=0, label='Pages')
#     is_available = forms.BooleanField(required=False, initial=True)
#     publishing_date = forms.DateField(label='Publishing Date')
#     description = forms.CharField(widget=forms.Textarea, label='Description')
#     image_url = forms.ImageField(label='Image')

class BookBaseFormBasic(forms.ModelForm):
    price = forms.DecimalField(max_digits=6, decimal_places=2, validators=[ValidatePrice()])

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Book Title',
            'price': 'Book Price',
            'isbn': 'ISBN',
            'is_available': 'Available'
        }
        help_texts = {
            'isbn': 'Must be unique',
            'genre': "Select from the drop-down menu",
            'language': "Select from the drop-down menu",

        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put the book title here'}),
        }
        error_messages = {
            'title': {
                'required': 'Please enter a valid book title.',
                'unique': 'This book already exists. Please provide a unique book title.',
            }
        }

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        if isbn and not isbn.startswith('978'):
            raise ValidationError('ISBN should start with 978')
        return isbn

    # def clean(self):
    #     cleaned_data = super().clean()
    #     if cleaned_data['title'].startswith('The') and cleaned_data['pages'] < 10:
    #         raise ValidationError('Fiction books should have at least 10 pages')
    #     return cleaned_data


class BookAddForm(BookBaseFormBasic):
    ...

class BookEditForm(BookBaseFormBasic):
    ...

class BookDeleteForm(BookBaseFormBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True