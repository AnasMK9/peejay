# Generated by Django 2.2.4 on 2019-08-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0003_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.CharField(max_length=40),
        ),
    ]
