# Generated by Django 3.0.6 on 2020-08-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_auto_20200808_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=None, max_length=32),
        ),
    ]
