# Generated by Django 3.0.7 on 2020-12-07 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_user',
        ),
    ]
