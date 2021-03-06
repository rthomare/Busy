# Generated by Django 3.0.5 on 2020-04-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_person_gif_search_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gif_search_type',
            field=models.CharField(choices=[('RAW_URL', 'URL'), ('GIPHY_TOP_SEARCH', 'Giphy Top Search'), ('GIPHY_RANDOM_SEARCH', 'Giphy Random Search')], default='RAW_URL', max_length=100),
        ),
    ]
