# Generated by Django 5.0.4 on 2024-06-15 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spamIdentifier', '0006_alter_registereduser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='user_permissions',
        ),
    ]
