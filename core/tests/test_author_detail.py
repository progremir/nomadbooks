from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.tests.factories import AuthorFactory
from users.tests.factories import UserFactory, TokenFactory


class AuthorDetailTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        author = AuthorFactory(id=999, name='Steven King')
        self.url = reverse('v1:author-detail', kwargs={'pk': author.pk})

    def test_author_detail_returns_401_given_anonymous_request(self):
        response = self.client.get(self.url)

        self.assertEqual(401, response.status_code)

    def test_author_detail_returns_200_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_author_detail_returns_valid_response_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        expected_response = {
            'id': 999,
            'name': 'Steven King',
        }

        response = self.client.get(self.url)

        self.assertEqual(expected_response, response.json())
