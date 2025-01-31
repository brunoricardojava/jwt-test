import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestJwtApi:
    """Test JWT API"""

    def test_user_access_with_token_correct_role(self, create_test_user_group_fixture, get_access_token_fixture):
        token = get_access_token_fixture

        url = reverse("user_view")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_user_access_with_token_incorrect_role(self, create_admin_user_group_fixture, get_admin_access_token_fixture):
        token = get_admin_access_token_fixture

        url = reverse("user_view")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(url)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.content == b'{"detail":"You do not have permission to perform this action."}'

    def test_user_access_without_token(self, create_test_user_group_fixture):
        url = reverse("user_view")
        client = APIClient()
        response = client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.content == b'{"detail":"Authentication credentials were not provided."}'

    def test_admin_access_with_token_correct_role(self, create_admin_user_group_fixture, get_admin_access_token_fixture):
        token = get_admin_access_token_fixture

        url = reverse("admin_view")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_admin_access_with_token_incorrect_role(self, create_test_user_group_fixture, get_access_token_fixture):
        token = get_access_token_fixture

        url = reverse("admin_view")
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(url)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.content == b'{"detail":"You do not have permission to perform this action."}'

    def test_admin_access_without_token(self, create_admin_user_group_fixture):
        url = reverse("admin_view")
        client = APIClient()
        response = client.get(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.content == b'{"detail":"Authentication credentials were not provided."}'

