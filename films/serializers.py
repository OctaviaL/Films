from rest_framework import serializers
from .models import Film, Category
from feedback.serializers import LikeSerializer
from feedback.models import Like



class FilmSerializer(serializers.ModelSerializer):

    likes = LikeSerializer(many=True,read_only=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post):
        return Like.objects.filter(post_id=post).count()


    class Meta:
        model = Film
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'