from django.contrib import admin

from movies.models import Movie, Rating, Catalog


admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Catalog)
