# Generated by Django 3.0.5 on 2020-06-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_attendance_system', '0003_faculty_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Faculty_Images/'),
        ),
    ]