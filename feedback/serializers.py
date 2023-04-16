from rest_framework import serializers
from feedback.models import Like, Rating, Favorite, Comment




class LikeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Like
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating 
        fields = ('rating', )

        
class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Favorite
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(required=False)
    class Meta:
        model = Comment
        fields = '__all__'