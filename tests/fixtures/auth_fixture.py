from pytest import fixture
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient


@fixture
def create_test_user_fixture():
    user = User.objects.create_user(username="user", password="password")
    return user

@fixture
def get_access_token_fixture():
    credentials = {"username": "user", "password": "password"}
    url = reverse("token_obtain_pair")
    response = APIClient().post(url, credentials)
    return response.data.get("access")

@fixture
def get_refresh_token_fixture():
    credentials = {"username": "user", "password": "password"}
    url = reverse("token_obtain_pair")
    response = APIClient().post(url, credentials)
    return response.data.get("refresh")
