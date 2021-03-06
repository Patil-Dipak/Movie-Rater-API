from enum import unique
from django.db import models
from django.contrib.auth.models import User     # for User db
from django.core.validators import MaxValueValidator, MinValueValidator

# Movie table
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    # Number of ratings
    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie = self)
        return len(ratings)

    # avg ratings method
    def avg_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(movie = self)
        for rating in ratings:
            sum +=  rating.stars
        if len(ratings) > 0:  
            return sum /len(ratings)
        else:
            return 0

#Rating table
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)    # ForeignKey of Movie table
    user = models.ForeignKey(User, on_delete= models.CASCADE)      #ForeignKey of User table
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)
