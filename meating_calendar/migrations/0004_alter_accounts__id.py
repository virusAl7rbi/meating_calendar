# Generated by Django 3.2.8 on 2021-10-18 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meating_calendar', '0003_auto_20211018_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='_id',
            field=models.PositiveIntegerField(default=0, editable=False, unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
