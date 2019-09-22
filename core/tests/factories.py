import factory

from core.models import Category, Author


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category


class AuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Author
