# Generated by Django 2.2.4 on 2019-08-24 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('req', '0006_auto_20190824_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='allreqs',
            name='reqtype',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='req1',
            name='reqtype',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
