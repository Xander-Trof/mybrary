from django.db import models
from django.db.models import Manager

# Create your models here.


class ReadBooksManager(Manager):
    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(
            read=True
        )


class FutureBooksManager(Manager):
    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(
            read=False
        )


class Books(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey('Authors', on_delete=models.SET_NULL)
    category = models.ManyToManyField('Categories')
    rating = models.ForeignKey('Rates', on_delete=models.SET_NULL)
    read = models.BooleanField()

    objects = Manager()
    read_manager = ReadBooksManager()
    unread_manager = FutureBooksManager()

    def mark_read(self, commit=True):
        self.read = True
        if commit:
            self.save()

    def __str__(self):
        return self.id


class Authors(models.Model):
    full_name = models.CharField(max_length=50)
    # book = models.ForeignKey('Books', on_delete=models.SET_NULL)

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

