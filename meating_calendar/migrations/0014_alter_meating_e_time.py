# Generated by Django 3.2.8 on 2021-10-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meating_calendar', '0013_alter_meating_e_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meating',
            name='e_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
