# Generated by Django 3.0.5 on 2020-06-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_attendance_system', '0011_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='date_created',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
