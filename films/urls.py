from django.urls import path, include
from .views import FilmModelViewSet, CategoryAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', FilmModelViewSet)
router.register('category', CategoryAPIView)

urlpatterns = [
    path('', include(router.urls))
]