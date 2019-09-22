import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.models import Author
from core.tests.factories import AuthorFactory
from users.tests.factories import UserFactory, TokenFactory


class AuthorUpdateTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        author = AuthorFactory(name='Old name')
        self.url = reverse('v1:author-detail', kwargs={'pk': author.pk})

    def test_author_update_returns_401_given_anonymous_request(self):
        body = {
            'name': 'Steven King',
        }
        response = self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(401, response.status_code)

    def test_author_update_returns_403_given_non_admin_user(self):
        user = UserFactory(is_staff=False)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Steven King',
        }
        response = self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(403, response.status_code)

    def test_author_update_returns_200_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Steven King',
        }
        response = self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertEqual(200, response.status_code)

    def test_author_update_updates_a_author_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        body = {
            'name': 'Steven King',
        }
        self.client.patch(self.url, json.dumps(body), content_type='application/json')

        self.assertTrue(Author.objects.filter(name='Steven King').exists())
