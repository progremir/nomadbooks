import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.models import Category
from core.tests.factories import CategoryFactory
from users.tests.factories import UserFactory, TokenFactory


class CategoryUpdateTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        category = CategoryFactory(name='Old name', description='Old description')
        self.url = reverse('v1:category-detail', kwargs={'pk': category.pk})

    def test_category_update_returns_401_given_anonymous_request(self):
        body = {
            'name': 'Drama',
            'description': 'Titanic stuff'
        }
        response = self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(401, response.status_code)

    def test_category_update_returns_403_given_non_admin_user(self):
        user = UserFactory(is_staff=False)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Drama',
            'description': 'Titanic stuff'
        }
        response = self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(403, response.status_code)

    def test_category_update_returns_200_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Drama',
            'description': 'Titanic stuff'
        }
        response = self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(200, response.status_code)

    def test_category_update_updates_a_category_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Drama',
            'description': 'Titanic stuff'
        }
        self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertTrue(Category.objects.filter(name='Drama', description='Titanic stuff').exists())
