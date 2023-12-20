import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="testuser", 
        password="testpassword"
    )
    return user
