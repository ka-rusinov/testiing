from rest_framework.serializers import ModelSerializer

from AuthToken.models import AuthToken


class AuthSerializer(ModelSerializer):
    class Meta:
        model = AuthToken
        fields = '__all__'