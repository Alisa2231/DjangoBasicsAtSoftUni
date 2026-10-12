from django import forms

from books.models import Book


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

class BookAddForm(BookBaseFormBasic):
    ...

class BookEditForm(BookBaseFormBasic):
    ...

class BookDeleteForm(BookBaseFormBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True