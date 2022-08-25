from django.contrib.auth.forms import UserCreationForm

from book_auth_app.models import CustomUser


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
        ]
