# Generated by Django 3.0.8 on 2021-06-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210601_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_file',
            field=models.ImageField(upload_to='media'),
        ),
    ]
