# Generated by Django 5.0.4 on 2024-06-15 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spamIdentifier', '0005_alter_registereduser_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registereduser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='registereduser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='registereduser',
            name='last_name',
        ),
    ]
