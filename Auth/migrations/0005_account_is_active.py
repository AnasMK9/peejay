# Generated by Django 2.2.4 on 2019-08-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    
    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('Auth', '0004_account_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
