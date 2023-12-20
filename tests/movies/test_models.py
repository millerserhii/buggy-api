import pytest

from movies.models import Movie, Rating, Catalog


@pytest.mark.django_db
def test_movie_model():
    movie = Movie.objects.create(
        title="The Matrix",
        genre="Sci-Fi",
        year=1999,
    )
    assert str(movie) == "The Matrix"


@pytest.mark.django_db
def test_rating_model(user):
    movie = Movie.objects.create(
        title="The Matrix",
        genre="Sci-Fi",
        year=1999,
    )
    rating = Rating.objects.create(
        movie=movie,
        user_id=user.id,
        rating=5,
        comment="Awesome movie",
    )
    assert str(rating) == "Awesome movie"
    
    with pytest.raises(NotImplementedError):
        rating.get_average_rating()
        

@pytest.mark.django_db
def test_catalog_model(user):
    movie = Movie.objects.create(
        title="The Matrix",
        genre="Sci-Fi",
        year=1999,
    )
    
    catalog = Catalog.objects.create(
        user=user,
    )
    catalog.movie.add(movie)
    
    assert str(catalog) == f"catalog for {user}"
    assert catalog.is_locked == False
    
    with pytest.raises(NotImplementedError):
        catalog.lock_catalog()
        