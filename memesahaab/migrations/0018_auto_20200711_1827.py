# Generated by Django 3.0.7 on 2020-07-11 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memesahaab', '0017_auto_20200711_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='meme_loss',
        ),
        migrations.RemoveField(
            model_name='like',
            name='meme_mememan',
        ),
        migrations.RemoveField(
            model_name='like',
            name='meme_surreal',
        ),
    ]
