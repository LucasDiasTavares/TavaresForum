from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questions.api import views

router = DefaultRouter()
router.register(r"questions", views.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls))
]
