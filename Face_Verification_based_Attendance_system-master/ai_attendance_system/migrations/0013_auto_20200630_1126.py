# Generated by Django 3.0.5 on 2020-06-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_attendance_system', '0012_auto_20200629_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='branch',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='section',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(default='Absent', max_length=200, null=True),
        ),
    ]
