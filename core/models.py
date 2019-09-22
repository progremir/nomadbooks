import uuid

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampModel

User = get_user_model()


def upload_to(_, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'/covers/{filename}'


class Category(TimestampModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Author(TimestampModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Book(TimestampModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author)
    read_by = models.ManyToManyField(User)
    cover = models.ImageField(upload_to=upload_to)

    class Meta:
        ordering = ('title',)
        default_related_name = 'books'


class Review(TimestampModel):
    rating = models.PositiveSmallIntegerField()
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        default_related_name = 'reviews'
