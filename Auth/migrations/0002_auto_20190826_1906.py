# Generated by Django 2.2.4 on 2019-08-26 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='BDate',
        ),
        migrations.RemoveField(
            model_name='account',
            name='hasAcc',
        ),
        migrations.RemoveField(
            model_name='account',
            name='sex',
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default='<function now at 0x7f9df9debd08>', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default='<function now at 0x7f9df9debd08>', max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='NID',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1000000000, django.core.validators.MaxValueValidator(9999999999))]),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]