# Generated by Django 2.2.4 on 2019-08-26 19:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0003_auto_20190826_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='expDate',
            field=models.DateField(default=datetime.date(2016, 9, 18)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='issueDate',
            field=models.DateField(verbose_name=datetime.date(2011, 1, 22)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='licenseNo',
            field=models.IntegerField(default=48355898, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]