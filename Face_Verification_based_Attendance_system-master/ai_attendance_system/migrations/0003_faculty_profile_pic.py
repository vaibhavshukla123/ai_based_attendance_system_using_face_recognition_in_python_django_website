# Generated by Django 3.0.5 on 2020-06-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_attendance_system', '0002_attendance_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Student_Images/'),
        ),
    ]
