from django.contrib import admin

from book_app.models import Books
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'rating',
        'read',
    )


admin.site.register(Books, BooksAdmin)
