from django import forms
from book_app.models import Books, Authors


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = [
            'full_name',
        ]


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = [
            'author',
        ]

    def save(self, commit=True, author=None):
        if author is None:
            raise ValueError('authors name was not set')

        inst = super().save(commit=False)
        inst.author = author

        if commit:
            inst.save()

        return inst
