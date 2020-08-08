# Generated by Django 3.0.6 on 2020-08-08 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200808_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Subject'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Subject'),
        ),
    ]
