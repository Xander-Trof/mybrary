from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    books = models.ForeignKey(
        'book_app.Books',
        null=True,
        default=None,
        blank=True,
        on_delete=models.CASCADE
    )
