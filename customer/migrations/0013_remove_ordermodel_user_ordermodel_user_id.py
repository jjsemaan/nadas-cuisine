# Generated by Django 4.2.11 on 2024-04-14 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='user',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]