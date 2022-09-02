from django.contrib import admin

from book_app.models import Books
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'get_tags',
        'read',
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())


admin.site.register(Books, BooksAdmin)
