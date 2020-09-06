# Generated by Django 3.0.3 on 2020-09-06 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveApp', '0015_auto_20200906_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='approved',
            field=models.CharField(choices=[('Approve', 'Approve'), ('Pending', 'Pending'), ('Decline', 'Decline')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='leave',
            name='req_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 6, 20, 49, 23, 984039)),
        ),
    ]