from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from core.models import Category
from core.tests.factories import CategoryFactory
from users.tests.factories import UserFactory, TokenFactory


class CategoryDeleteTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        category = CategoryFactory(name='Drama', description='Titanic stuff')
        self.url = reverse('v1:category-detail', kwargs={'pk': category.pk})

    def test_category_update_returns_401_given_anonymous_request(self):
        response = self.client.delete(self.url)

        self.assertEqual(401, response.status_code)

    def test_category_update_returns_403_given_non_admin_user(self):
        user = UserFactory(is_staff=False)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.delete(self.url)

        self.assertEqual(403, response.status_code)

    def test_category_update_returns_204_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.delete(self.url)

        self.assertEqual(204, response.status_code)

    def test_category_update_deletes_a_category_given_valid_input(self):
        user = UserFactory(is_staff=True)
        token = TokenFactory(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.client.delete(self.url)

        self.assertFalse(Category.objects.exists())
