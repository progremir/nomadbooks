import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.models import Author
from users.tests.factories import UserFactory, TokenFactory


class AuthorCreateTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse('v1:author-list')

    def test_author_create_returns_401_given_anonymous_request(self):
        body = {
            'name': 'Steven King'
        }
        response = self.client.post(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(401, response.status_code)

    def test_author_create_returns_403_given_non_admin_user(self):
        user = UserFactory(is_staff=False)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Steven King'
        }
        response = self.client.post(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(403, response.status_code)

    def test_author_create_returns_201_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Steven King'
        }
        response = self.client.post(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(201, response.status_code)

    def test_author_create_creates_an_author_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Steven King'
        }
        self.client.post(self.url, json.dumps(body), content_type='application/json')

        self.assertTrue(Author.objects.exists())
