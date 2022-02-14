import json
from unittest import result

from django.http  import JsonResponse
from django.views import View

from movies.models import Actor, Movie, Actor_Movie

class ActorsView(View):
    def get(self, request):
        actors   = Actor.objects.all()
        results  = []
        for actor in actors:
            movie_lists = []
            movies      = actor.movies.all()
            for movie in movies:
                movie_lists.append({
                    "title" : movie.title
                })
            results.append({
                "first_name" : actor.first_name,
                "last_name" : actor.last_name,
                "movie" : movie_lists
            })

        return JsonResponse({'resutls':results}, status=200)

class MoviesView(View):
    def get(self, request):
        movies   = Movie.objects.all()
        results  = []
        for movie in movies:
            actor_lists = []
            actors      = movie.actor_set.all()
            for actor in actors:
                actor_lists.append({
                    "name" : actor.first_name
                })
            results.append(
                {
                   "title" : movie.title,
                   "running_time" : movie.running_time,
                   "actor" : actor_lists
                }
            )
       
        return JsonResponse({'resutls':results}, status=200)
