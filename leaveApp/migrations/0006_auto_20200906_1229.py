# Generated by Django 3.0.3 on 2020-09-06 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveApp', '0005_auto_20200906_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='req_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 6, 12, 29, 27, 621314)),
        ),
    ]
