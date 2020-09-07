from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questions.api.views import (QuestionViewSet,
                                 AnswerCreateAPIView,
                                 AnswerAPIView,
                                 AnswerRUDAAPIView,
                                 AnswerLikeAPIView)

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("questions/<slug:slug>/answers/",
         AnswerAPIView.as_view(), name="answer-list"),
    path("questions/<slug:slug>/answer/",
         AnswerCreateAPIView.as_view(), name="answer-create"),
    path("answers/<int:pk>/",
         AnswerRUDAAPIView.as_view(), name="answer-detail"),
    path("answers/<int:pk>/like/",
         AnswerLikeAPIView.as_view(), name="answer-like"),
]
