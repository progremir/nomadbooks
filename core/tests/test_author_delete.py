from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.models import Author
from core.tests.factories import AuthorFactory
from users.tests.factories import UserFactory, TokenFactory


class AuthorDeleteTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        author = AuthorFactory(name='Steven King')
        self.url = reverse('v1:author-detail', kwargs={'pk': author.pk})

    def test_author_update_returns_401_given_anonymous_request(self):
        response = self.client.delete(self.url)

        self.assertEqual(401, response.status_code)

    def test_author_update_returns_403_given_non_admin_user(self):
        user = UserFactory(is_staff=False)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.delete(self.url)

        self.assertEqual(403, response.status_code)

    def test_author_update_returns_204_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.delete(self.url)

        self.assertEqual(204, response.status_code)

    def test_author_update_deletes_a_author_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.client.delete(self.url)

        self.assertFalse(Author.objects.exists())
