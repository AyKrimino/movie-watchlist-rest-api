# Generated by Django 5.0.3 on 2024-04-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
