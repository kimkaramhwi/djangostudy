import json
from unittest import result

from django.http  import JsonResponse
from django.views import View

from movies.models import Actor, Movie

class ActorsView(View):
    def get(self, request):
        actors   = Actor.objects.all() # actor테이블의 모든 레코드를 querySet으로 가져온다.
        results  = [] # 배우의 이름과 성, 출연한 영화 제목 목록을 출력할 리스트
        for actor in actors: # actor테이블의 모든 레코드를 돈다.
            movie_lists = [] # movie를 담을 리스트 생성
            movies      = actor.movies.all() # MTM관계 지정을 했으므로 중간 테이블없이 movies 값을 가져올 수 있다.
            for movie in movies: # movie테이블의 모든 레코드를 돈다.
                movie_lists.append({ # 영화 제목을 영화 리스트에 추가한다.
                    "title" : movie.title # 영화 제목을 가져온다.
                })
            results.append({ # 배우의 이름, 영화 목록을 추가한다.
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
            actor_lists = [] # actor를 담을 리스트 생성
            actors      = movie.actor_set.all() # movie에서 actor 참조는 역참조이다.
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
