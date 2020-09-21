from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.api.serializers import QuestionSerializers, AnswerSerializers
from questions.models import Question, Answer
from questions.api.permissions import IsAuthorOrReadyOnly


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializers
    permission_classes = [IsAuthenticated, IsAuthorOrReadyOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this Question!")

        serializer.save(author=request_user, question=question)


class AnswerAPIView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")


class AnswerRUDAAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [IsAuthenticated, IsAuthorOrReadyOnly]


class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializers
    permission_classes = [IsAuthenticated]

    # pk is a parameter from my endpoint
    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user
        answer.voters.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user
        answer.voters.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

