# Generated by Django 2.0.2 on 2018-03-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luda', '0005_auto_20180306_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmy',
            name='update_time',
            field=models.CharField(default='', max_length=9999),
        ),
        migrations.AddField(
            model_name='my',
            name='update_time',
            field=models.CharField(default='', max_length=9999),
        ),
    ]
