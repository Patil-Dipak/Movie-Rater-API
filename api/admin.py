from django.contrib import admin
from . models import Movie, Rating

# Register the model

admin.site.register(Movie)
admin.site.register(Rating)