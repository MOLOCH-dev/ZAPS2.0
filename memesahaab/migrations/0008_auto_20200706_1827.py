# Generated by Django 3.0.7 on 2020-07-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memesahaab', '0007_catg_meme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catg_meme',
            name='author',
            field=models.TextField(),
        ),
    ]
