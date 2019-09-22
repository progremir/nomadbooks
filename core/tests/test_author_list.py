from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.tests.factories import AuthorFactory
from users.tests.factories import UserFactory, TokenFactory


class AuthorListTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse('v1:author-list')

    def test_author_list_returns_401_given_anonymous_request(self):
        response = self.client.get(self.url)

        self.assertEqual(401, response.status_code)

    def test_author_list_returns_200_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_author_list_returns_valid_response_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        AuthorFactory(id=999, name='Steven King')
        expected_response = {
            'total_count': 1,
            'total_pages': 1,
            'list': [
                {
                    'id': 999,
                    'name': 'Steven King',
                }
            ]
        }
        response = self.client.get(self.url)

        self.assertTrue(expected_response, response.json())
