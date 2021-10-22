from rest_framework.serializers import ModelSerializer

from ReadOnlyUserSerializer.models import ReadOnlyUserSerializer


class ReadSerializer(ModelSerializer):
    class Meta:
        model = ReadOnlyUserSerializer
        fields = '__all__'