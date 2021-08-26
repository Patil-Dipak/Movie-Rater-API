from django.urls import path, include
from rest_framework import routers
from . views import MovieViewSet, RatingViewSet

router = routers.DefaultRouter()
# Register the viewsets
router.register('movies', MovieViewSet)
router.register('Ratings', RatingViewSet)

urlpatterns = [
     path('', include(router.urls)),
]