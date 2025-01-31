from pytest import fixture
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from django.contrib.auth.models import Group


@fixture
def create_test_user_fixture():
    user = User.objects.create_user(username="user", password="password")
    return user

@fixture
def create_test_admin_user_fixture():
    user = create_test_user_fixture(username="admin", password="password")
    return user

@fixture
def create_user_group_fixture():
    group, _ = Group.objects.get_or_create(name="user")
    return group

@fixture
def create_admin_group_fixture():
    group, _ = Group.objects.get_or_create(name="admin")
    return group

@fixture
def create_test_user_group_fixture(create_test_user_fixture, create_user_group_fixture):
    user = create_test_user_fixture
    group = create_user_group_fixture
    user.groups.add(group)
    return user

@fixture
def create_admin_user_group_fixture(create_admin_group_fixture):
    user = User.objects.create_user(username="admin", password="password")
    group = create_admin_group_fixture
    user.groups.add(group)
    return user

@fixture
def get_access_token_fixture(credentials={"username": "user", "password": "password"}):
    url = reverse("token_obtain_pair")
    response = APIClient().post(url, credentials)
    return response.data.get("access")

@fixture
def get_admin_access_token_fixture(credentials={"username": "admin", "password": "password"}):
    url = reverse("token_obtain_pair")
    response = APIClient().post(url, credentials)
    return response.data.get("access")

@fixture
def get_refresh_token_fixture(credentials={"username": "user", "password": "password"}):
    url = reverse("token_obtain_pair")
    response = APIClient().post(url, credentials)
    return response.data.get("refresh")

@fixture
def get_admin_refresh_token_fixture(credentials={"username": "admin", "password": "password"}):
    url = reverse("token_obtain_pair")
    response = APIClient().post(url, credentials)
    return response.data.get("refresh")
