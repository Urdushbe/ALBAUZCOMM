# Generated by Django 4.2.3 on 2023-08-12 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='job',
            name='is_daily',
        ),
    ]
