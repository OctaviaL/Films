from rest_framework.permissions import IsAdminUser
from .models import Film, Category
from .serializers import FilmSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from feedback.models import Like

class FilmModelViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['POST'], detail=True) #localhost:8000/api/v1/post/1/like
    def like(self, request, pk, *args, **kwargs):
        user = request.user
        print(user)
        print(pk)
        like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'
        if not like_obj.is_like:
            status = 'unliked'
        return Response({'status': status})
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
