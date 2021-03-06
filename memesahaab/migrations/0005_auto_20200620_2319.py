# Generated by Django 3.0.7 on 2020-06-20 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memesahaab', '0004_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={},
        ),
        migrations.RemoveField(
            model_name='categories',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='meme',
        ),
        migrations.AddField(
            model_name='categories',
            name='Categories_list',
            field=models.CharField(choices=[('CG0', 'c'), ('CG1', 'a'), ('CG2', 't'), ('CG3', 'e'), ('CG4', 'g'), ('CG5', 'o'), ('CG6', 'r'), ('CG7', 'i'), ('CG8', 's')], default=None, max_length=100),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('meme_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memesahaab.Meme')),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='categories',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='memesahaab.Category'),
            preserve_default=False,
        ),
    ]
