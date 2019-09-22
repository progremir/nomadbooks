from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.tests.factories import CategoryFactory
from users.tests.factories import UserFactory, TokenFactory


class CategoryListTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse('v1:category-list')

    def test_category_list_returns_401_given_anonymous_request(self):
        response = self.client.get(self.url)

        self.assertEqual(401, response.status_code)

    def test_category_list_returns_200_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_category_list_returns_valid_response_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        CategoryFactory(id=999, name='Drama', description='Titanic stuff')
        expected_response = {
            'total_count': 1,
            'total_pages': 1,
            'list': [
                {
                    'id': 999,
                    'name': 'Drama',
                    'description': 'Titanic stuff'
                }
            ]
        }
        response = self.client.get(self.url)

        self.assertTrue(expected_response, response.json())
