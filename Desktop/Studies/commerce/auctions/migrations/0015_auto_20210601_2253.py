# Generated by Django 3.0.8 on 2021-06-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210601_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
