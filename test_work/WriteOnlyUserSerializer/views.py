from venv import create

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from WriteOnlyUserSerializer.models import WriteOnlyUserSerializer


class WriteSerializerView(ModelViewSet):
    permissions_classes = [IsAuthenticated]
    queryset = WriteOnlyUserSerializer.objects.all()
    serializer_class = WriteOnlyUserSerializer()

    def post_get(self, request, format=None):
        if request.method == 'GET':
            serializer = WriteOnlyUserSerializer(request)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = WriteOnlyUserSerializer(request, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            WriteOnlyUserSerializer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
