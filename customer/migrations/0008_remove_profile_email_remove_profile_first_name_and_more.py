# Generated by Django 4.2.11 on 2024-04-13 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
