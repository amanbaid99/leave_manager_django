# Generated by Django 3.1.1 on 2020-09-05 17:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='e_type',
            field=models.CharField(choices=[('em', 'employee'), ('mn', 'manager')], default='em', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='no_of_leaves',
            field=models.IntegerField(default=24, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)]),
        ),
    ]