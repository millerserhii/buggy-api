import pytest
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from movies.models import Movie


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="testuser", 
        password="testpassword"
    )
    return user

@pytest.fixture
def movie():
    movie = Movie.objects.create(
        title="Test Movie",
        genre="Test Genre",
        year="2021",
    )
    return movie
