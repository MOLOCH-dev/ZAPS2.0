# Generated by Django 3.0.7 on 2020-07-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memesahaab', '0013_mememan_meme_surreal_meme'),
    ]

    operations = [
        migrations.AddField(
            model_name='loss_meme',
            name='loss_meme_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mememan_meme',
            name='mememan_meme_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surreal_meme',
            name='surreal_meme_comments',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
