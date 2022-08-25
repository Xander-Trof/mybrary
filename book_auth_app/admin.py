from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from book_auth_app.models import CustomUser
# Register your models here.


class CustomAdminModel(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Books', {'fields': (
        #     'title',
        #     'author',
        #     'category',
        #     'rating',
        #     'read',
        )}),
    )
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'books',
    )
    list_editable = ()
    list_filter = (
        # 'book__title',
    )
    search_fields = (
        'first_name',
        'last_name',
        'username',
    )


admin.site.register(CustomUser, CustomAdminModel)
