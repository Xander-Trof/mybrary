from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.db import transaction

from mybrary_app.models import Books, Authors
from mybrary_app.forms import BooksForm, AuthorForm

# Create your views here.


def index(request):
    if request.method == 'GET':
        books = Books.objects.all()
        return render(request, 'mybrary_app/index.html', {'books': books})

    return HttpResponse(status=405)


def add_book(request):
    if request.method == 'GET':
        c = {
            'book_form': BooksForm(),
            'author_form': AuthorForm(),
        }
        return render(request, 'mybrary_app/add-book.html', c)

    elif request.method == 'POST':
        book_form = BooksForm(request.POST)
        author_form = AuthorForm(request.POST)

        if book_form.is_valid() and author_form.is_valid():
            with transaction.atomic():
                author = author_form.save()
                book = book_form.save(author=author)
                book_form.save_m2m()

            return redirect(reverse('index'))
