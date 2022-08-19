from django import forms
from mybrary_app.models import Books


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = []