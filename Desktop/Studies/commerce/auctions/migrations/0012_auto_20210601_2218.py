# Generated by Django 3.0.8 on 2021-06-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auctioned_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image_link',
        ),
        migrations.AddField(
            model_name='listing',
            name='image_file',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]