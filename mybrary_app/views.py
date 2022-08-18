from django.shortcuts import render
from django.http import HttpResponse

from models import Books

# Create your views here.


def index(request):
    if request.method == 'GET':
        books = Books.objects.all()
        return render(request, 'mybrary_app/index.html', books)
    return HttpResponse("It's not working")
