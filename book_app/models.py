from django.db import models

from django.conf import settings
from taggit.managers import TaggableManager
from book_auth_app.models import CustomUser

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=300)

    # Linking
    author = models.ForeignKey('Authors', on_delete=models.PROTECT)
    rating = models.ForeignKey('Rates', on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tags = TaggableManager()

    # Utils
    read = models.BooleanField()

    def mark_read(self, commit=True):
        self.read = True
        if commit:
            self.save()

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Authors(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.full_name)


class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return str(self.category)


class Rates(models.Model):
    BAD = ('B', 'bad')
    GOOD = ('G', 'good')
    EXCELLENT = ('E', 'excellent')
    __all = dict([BAD, GOOD, EXCELLENT])

    rate = models.CharField(max_length=2, choices=__all.items())

    def __str__(self):
        return str(self.__all[self.rate])
