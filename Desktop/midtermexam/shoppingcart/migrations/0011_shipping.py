# Generated by Django 3.0.8 on 2021-04-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0010_auto_20210406_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_weight', models.IntegerField()),
                ('max_weight', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]