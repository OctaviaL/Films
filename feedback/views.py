from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from feedback.models import Comment, Like, Rating
from feedback.serializers import CommentSerializer, RatingSerializer, LikeSerializer, FavoriteSerializer
from films.models import Film

class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = []
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return super().get_queryset()

class LikeAPIView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = []
    permission_classes = [IsAuthenticated]
    def like(self, request, pk, *args, **kwargs):
        like_obj, _ = Like.objects.get_or_create(post_id=pk, user=request.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unliked'
        return Response({'status': status})
    def get_queryset(self):
        return super().get_queryset()


class RatingAPIView(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = []
    permission_classes = [IsAuthenticated]
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(post_id=pk, user=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return super().get_queryset()

class FavoriteAPIView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = FavoriteSerializer
    authentication_classes = []
    permission_classes = [IsAuthenticated]

    def favorite(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Film, id=id)
        if product.favorite.filter(id=request.user.id).exists():
            product.favorite.remove(request.user)
        else:
            product.favorite.add(request.user)
        return Response(request.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return super().get_queryset()