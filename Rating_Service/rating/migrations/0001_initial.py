# Generated by Django 3.2 on 2021-06-27 00:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('hotel_likes', models.IntegerField(default=0)),
                ('hotel_dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LikeHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_uid', models.UUIDField(default=uuid.uuid4)),
                ('hotel_uid', models.UUIDField(default=uuid.uuid4)),
                ('like', models.BooleanField(default=False)),
                ('dislike', models.BooleanField(default=False)),
            ],
        ),
    ]
