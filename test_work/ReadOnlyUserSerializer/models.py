from django.core.validators import MinLengthValidator
from django.db import models


class ReadOnlyUserSerializer(models.Model):
    username = models.CharField('Username', max_length=150, validators=[MinLengthValidator(1)])
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=150)

