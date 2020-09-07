from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from questions.api.serializers import QuestionSerializers
from questions.models import Question
from questions.api.permissions import IsAuthorOrReadyOnly


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializers
    permission_classes = [IsAuthenticated, IsAuthorOrReadyOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

