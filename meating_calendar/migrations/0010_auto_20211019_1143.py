# Generated by Django 3.2.8 on 2021-10-19 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meating_calendar', '0009_alter_meating_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meating',
            name='room',
        ),
        migrations.AddField(
            model_name='meating',
            name='building_choices',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meating_calendar.meating_room'),
        ),
    ]
