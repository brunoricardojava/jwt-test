import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

@pytest.mark.usefixtures("create_test_user_fixture")
@pytest.mark.django_db
class TestJWTAuth:
    """Test JWT Authentication"""

    def test_token_generation_with_correct_credentials(self):
        credentials = {"username": "user", "password": "password"}
        url = reverse("token_obtain_pair")
        response = APIClient().post(url, credentials)

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data

    def test_token_generation_with_incorrect_credentials(self):
        credentials = {"username": "incorrect_user", "password": "incorrect_password"}
        url = reverse("token_obtain_pair")
        response = APIClient().post(url, credentials)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.content == b'{"detail":"No active account found with the given credentials"}'

    def test_token_generation_no_credentials(self):
        url = reverse("token_obtain_pair")
        response = APIClient().post(url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.content == b'{"username":["This field is required."],"password":["This field is required."]}'

    def test_token_refresh_with_correct_token(self, get_refresh_token_fixture):
        refresh_token = get_refresh_token_fixture
        url = reverse("token_refresh")
        response = APIClient().post(url, {"refresh": refresh_token})

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data

    def test_token_refresh_with_incorrect_token(self):
        refresh_token = "incorrect_refresh_token"
        url = reverse("token_refresh")
        response = APIClient().post(url, {"refresh": refresh_token})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.content == b'{"detail":"Token is invalid or expired","code":"token_not_valid"}'

    def test_token_refresh_no_token(self):
        url = reverse("token_refresh")
        response = APIClient().post(url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.content == b'{"refresh":["This field is required."]}'
