from django.urls import path
from recommendation.views import RecommendationView

urlpatterns = [

    path('', RecommendationView.as_view()),
]