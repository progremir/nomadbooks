import factory

from core.models import Category


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category
