# Generated by Django 4.0.2 on 2022-02-14 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_actors_movie_actors_actor_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
    ]
