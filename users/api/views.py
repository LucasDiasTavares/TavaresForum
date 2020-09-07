from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializers


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializers(request.user)
        return Response(serializer.data)
