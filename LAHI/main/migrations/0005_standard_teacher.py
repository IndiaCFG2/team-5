# Generated by Django 3.0.6 on 2020-08-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_standard_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='teacher',
            field=models.ManyToManyField(to='main.Teacher'),
        ),
    ]
