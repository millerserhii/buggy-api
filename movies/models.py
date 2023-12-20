from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment
    
    def get_average_rating(self):
        '''
        Get average rating for a movie
        '''
        raise NotImplementedError('Please implement this method')
    
    

class Catalog(models.Model):
    movie = models.ManyToManyField(Movie)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_locked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"catalog for {self.user}"
    
    def lock_catalog(self):
        '''
        Superuser can lock a user's catalog
        '''
        raise NotImplementedError('Please implement this method')
    