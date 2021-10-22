from rest_framework.viewsets import ModelViewSet

from AuthToken.authserializer import AuthSerializer
from AuthToken.models import AuthToken


class AuthTokenView(ModelViewSet):
    queryset = AuthToken.objects.all()
    serializer_class = AuthSerializer
