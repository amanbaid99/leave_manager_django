# Generated by Django 3.0.3 on 2020-09-07 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveApp', '0017_auto_20200906_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='approved_by',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='leave',
            name='req_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 12, 43, 12, 406011)),
        ),
    ]
