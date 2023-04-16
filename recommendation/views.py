from rest_framework.views import APIView
from .models import MovieRecomm
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer

User = get_user_model()

class RecommendationView(APIView):
    authentication_classes = []
    def get(self, request):
        user = request.user
        last_viewed_film = user.history.last().film
        similar_films = last_viewed_film.get_similar_films()
        favorite_genre_films = MovieRecomm.get_favorite_genre_films(user)
        new_release_films = MovieRecomm.get_new_release_films()
        recommended_films = list(similar_films) + list(favorite_genre_films) + list(new_release_films)
        serializer = MovieSerializer(recommended_films, many=True)
        return Response(serializer.data)
