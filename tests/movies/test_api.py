import pytest

from rest_framework.test import APIClient
from django.urls import reverse

from movies.models import Movie


@pytest.mark.django_db
def test_movie_list(api_client: APIClient, movie: Movie) -> None:
    url = reverse("movie-list")
    response = api_client.get(url)
    assert response.status_code == 200
    results = response.data.get("results")
    assert len(results) == 1
    assert results[0]["title"] == movie.title
    
@pytest.mark.django_db
def test_movie_detail(api_client: APIClient, movie: Movie) -> None:
    url = reverse("movie-detail", args=[movie.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["title"] == movie.title
    
@pytest.mark.django_db
def test_movie_create(api_client: APIClient) -> None:
    url = reverse("movie-list")
    data = {
        "title": "Test Movie",
        "genre": "Test Genre",
        "year": 2021,
    }
    response = api_client.post(url, data=data)
    assert response.status_code == 201
    assert response.data["title"] == data["title"]
    assert response.data["genre"] == data["genre"]
    assert response.data["year"] == data["year"]
    
@pytest.mark.django_db
def test_movie_create_invalid_year(api_client: APIClient) -> None:
    url = reverse("movie-list")
    data = {
        "title": "Test Movie",
        "genre": "Test Genre",
        "year": "invalid",
    }
    response = api_client.post(url, data=data)
    assert response.status_code == 400
    
@pytest.mark.django_db
def test_movie_update(api_client: APIClient, movie: Movie) -> None:
    url = reverse("movie-detail", args=[movie.id])
    data = {
        "title": "Updated Movie",
        "genre": "Updated Genre",
        "year": 2022,
    }
    response = api_client.put(url, data=data)
    assert response.status_code == 200
    assert response.data["title"] == data["title"]
    assert response.data["genre"] == data["genre"]
    assert response.data["year"] == data["year"]
    
    
@pytest.mark.django_db
def test_movie_delete(api_client: APIClient, movie: Movie) -> None:
    url = reverse("movie-detail", args=[movie.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Movie.objects.count() == 0
    