# Generated by Django 2.0.2 on 2018-03-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luda', '0004_auto_20180306_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.ImageField(null=True, upload_to='%Y-%m-%d/'),
        ),
    ]
