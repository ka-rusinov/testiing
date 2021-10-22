# Generated by Django 3.2.8 on 2021-10-22 04:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReadOnlyUserSerializer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Username')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
            ],
        ),
    ]
