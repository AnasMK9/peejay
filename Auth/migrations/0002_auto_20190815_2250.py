# Generated by Django 2.2.4 on 2019-08-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='hasAcc',
        ),
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default=123456789, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default=123456789, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
