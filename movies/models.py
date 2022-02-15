from django.db import models

class Actor(models.Model):
    first_name    = models.CharField(max_length=20)
    last_name     = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    movies        = models.ManyToManyField("Movie", through="Actor_Movie")
    # though를 지정해주지 않으면 다른 테이블로 접근할 때 매번 중간 테이블을 거쳐야한다.

    class Meta:
        db_table = 'actors'

class Actor_Movie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'

class Movie(models.Model):
    title        = models.CharField(max_length=20)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'