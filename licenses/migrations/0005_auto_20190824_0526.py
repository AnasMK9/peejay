# Generated by Django 2.2.4 on 2019-08-24 05:26

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0004_auto_20190824_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='expDate',
            field=models.DateField(default=datetime.date(2015, 12, 7)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='issueDate',
            field=models.DateField(verbose_name=datetime.date(2010, 5, 22)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='licenseNo',
            field=models.IntegerField(default=58895001, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]
