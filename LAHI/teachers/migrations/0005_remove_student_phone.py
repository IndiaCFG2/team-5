# Generated by Django 3.0.6 on 2020-08-08 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20200808_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
    ]
