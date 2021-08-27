from api.models import Movie
from rest_framework import viewsets, status
from rest_framework.response import Response
from . models import Movie, Rating
from . serializers import MovieSerializer, RatingSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    #Rate the movie
    @action(detail = True, methods = ['POST'])
    def rate_movie(self, request, pk = None):
        if 'stars' in request.data:     # if user provide the star in rating
            
            movie = Movie.objects.get(id = pk)
            stars = request.data['stars']
            user = User.objects.get(id = 1)

            try:
                rating = Rating.objects.get(user = user.id, movie = movie.id)
                rating.stars = stars
                rating.save()
                response = {'message': 'its working'}
                return Response(response, status = status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user = user.id, movie = movie.id, stars = stars)
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status = status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer