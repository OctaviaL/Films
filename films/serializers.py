from rest_framework import serializers
from .models import Film, Category, Image
from feedback.serializers import LikeSerializer
from feedback.models import Like

class FilmImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):

    images = FilmImageSerializers(many=True, read_only=True)
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

    def create(self, validated_data):
        request = self.context.get('request')
        film = Film.objects.create(**validated_data)
        files = request.FILES
        list_images = []
        for image in files.getlist('images'):
            list_images.append(Image(film=film, image=image))
        Image.objects.bulk_create(list_images) # sohranit odnim soedineniem razom vse kartinki
        return film