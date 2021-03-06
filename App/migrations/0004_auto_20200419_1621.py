# Generated by Django 3.0.5 on 2020-04-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200419_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gif_search_type',
            field=models.CharField(choices=[('RAW_URL', 'URL'), ('GIPHY_TOP_SEARCH', 'Giphy Top Search'), ('GIPHY_RANDOM_SEARCH', 'Giphy Random Search'), ('GIPHY_SHUFFLE_SEARCH', 'Giphy Shuffle Search')], default='RAW_URL', max_length=100),
        ),
    ]
