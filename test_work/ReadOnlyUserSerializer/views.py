from rest_framework.viewsets import ModelViewSet

from ReadOnlyUserSerializer.models import ReadOnlyUserSerializer


class ReadSerializerView(ModelViewSet):
    queryset = ReadOnlyUserSerializer.objects.all()
    serializer_class = ReadOnlyUserSerializer
