# Generated by Django 3.0.8 on 2020-08-08 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200808_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
