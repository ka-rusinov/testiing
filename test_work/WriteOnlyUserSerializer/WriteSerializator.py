from rest_framework.serializers import ModelSerializer

from WriteOnlyUserSerializer.models import WriteOnlyUserSerializer


class WriteSerializer(ModelSerializer):
    class Meta:
        model = WriteOnlyUserSerializer
        fields = '__all__'