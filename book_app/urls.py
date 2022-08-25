from django.urls import path
from book_app.views import add_book

urlpatterns = [
    path('add-book/', add_book, name='add_book')
]