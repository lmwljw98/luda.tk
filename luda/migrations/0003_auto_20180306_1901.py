# Generated by Django 2.0.2 on 2018-03-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luda', '0002_uploadfilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
