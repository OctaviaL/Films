from django.db import models
from django.contrib.auth import get_user_model
from films.models import Film

User = get_user_model()

class MovieRecomm(models.Model):

    def get_similar_films(self, limit=10):
        return Film.objects.exclude(pk=self.pk).filter(genre=self.genre)[:limit]

    @classmethod
    def get_favorite_genre_films(cls, user, limit=10):
        favorite_genre = user.favorite.genre
        return cls.objects.filter(genre=favorite_genre).order_by('-created_at')[:limit]

    @classmethod
    def get_new_release_films(cls, limit=10):
        return cls.objects.order_by('-created_at')[:limit]
