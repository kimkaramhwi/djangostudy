import json

from django.http  import JsonResponse
from django.views import View

from movies.models import Actor, Movie, Actor_Movie

class ActorsView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results  = []
        for movie in movies:
            actors_movies = Actor_Movie.objects.get(movie=movie.id)
            results.append(
               {
                   "first_name" : actors_movies.actor.first_name,
                   "last_name" : actors_movies.actor.last_name,
                   "title" : movie.title
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class MoviesView(View):

    def get(self, request):
        movies = Movie.objects.all()
        results  = []

        for movie in movies:
            actors_movies = Actor_Movie.objects.get(movie=movie.id)
            results.append(
                {
                   "title" : movie.title,
                   "running_time" : movie.running_time,
                   "first_name" : actors_movies.actor.first_name
                }
            )
       
        return JsonResponse({'resutls':results}, status=200)
