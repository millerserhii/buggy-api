from django.contrib import admin
from django.urls import include, path

from movies.urls import router as movies_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movie/', include(movies_router.urls)),
]