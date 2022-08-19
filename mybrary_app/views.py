from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from mybrary_app.models import Books
from mybrary_app.forms import BooksForm

# Create your views here.


def index(request):
    if request.method == 'GET':
        books = Books.objects.all()
        return render(request, 'mybrary_app/index.html', {'books': books})
    return HttpResponse(status=405)


def add_book(request):
    if request.method == 'GET':
        return render(request, 'mybrary_app/add-book.html', {'book_form': BooksForm()})

    elif request.method == 'POST':
        book_form = BooksForm(request.POST)

        if book_form.is_valid():
            book = book_form.save()

            return redirect(reverse('books:index'))
