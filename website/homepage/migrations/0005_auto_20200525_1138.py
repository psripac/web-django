# Generated by Django 3.0.6 on 2020-05-25 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20200525_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='sample_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 11, 38, 22, 918993), verbose_name='date published'),
        ),
    ]
