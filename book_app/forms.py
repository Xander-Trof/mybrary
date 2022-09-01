from django import forms
from book_app.models import Books, Authors


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = [
            'full_name',
        ]


class BooksForm(forms.ModelForm):
    # category = forms.fields.CharField(required=False)
    class Meta:
        model = Books
        exclude = [
            'author',
            'user',
        ]

    def save(self, commit=True, author=None, user=None):
        if author is None:
            raise ValueError('authors name was not set')
        if user is None:
            raise ValueError('user was not set')

        inst = super().save(commit=False)
        inst.author = author
        inst.user = user

        if commit:
            inst.save()

        return inst
