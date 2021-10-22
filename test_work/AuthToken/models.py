from django.core.validators import MinLengthValidator
from django.db import models


class AuthToken(models.Model):
    username = models.CharField('Username', max_length=255, validators=[MinLengthValidator(1)])
    password = models.CharField('Password', max_length=255, validators=[MinLengthValidator(1)])
