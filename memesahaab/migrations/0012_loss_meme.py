# Generated by Django 3.0.7 on 2020-07-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memesahaab', '0011_auto_20200707_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loss_Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('caption', models.TextField()),
                ('loss_meme', models.ImageField(blank=True, null=True, upload_to='uploaded.html')),
                ('loss_meme_file', models.FileField(upload_to='uploaded.html')),
            ],
        ),
    ]
