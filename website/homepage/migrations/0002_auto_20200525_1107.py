# Generated by Django 3.0.6 on 2020-05-25 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='sample_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 11, 7, 1, 129135), verbose_name='date published'),
        ),
    ]
