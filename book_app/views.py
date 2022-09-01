from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.db import transaction

from book_app.models import Books
from book_app.forms import BooksForm, AuthorForm

# Create your views here.


def index(request):
    if request.method == 'GET':
        user = request.user
        if str(user) == 'AnonymousUser':
            return render(request, 'book_app/index.html')
        else:
            # print(user, filtered_books)
            filtered_books = Books.objects.filter(user__exact=user)
            books = Books.objects.all()
            return render(request, 'book_app/index.html', {'books': filtered_books})

    return HttpResponse(status=405)


def add_book(request):
    if request.method == 'GET':
        c = {
            'book_form': BooksForm(),
            'author_form': AuthorForm(),
        }
        return render(request, 'book_app/add-book.html', c)

    elif request.method == 'POST':
        book_form = BooksForm(request.POST)
        author_form = AuthorForm(request.POST)
        user = request.user

        if book_form.is_valid() and author_form.is_valid():
            with transaction.atomic():
                author = author_form.save()
                book_form.save(user=user, author=author)
                book_form.save_m2m()

            return redirect(reverse('index'))
