# Generated by Django 3.0.3 on 2020-09-07 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveApp', '0018_auto_20200907_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='req_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 12, 59, 52, 739307)),
        ),
    ]
