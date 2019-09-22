import factory

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda x: f'username #{x}')

    class Meta:
        model = User


class TokenFactory(factory.DjangoModelFactory):
    class Meta:
        model = Token
