# Generated by Django 4.2.11 on 2024-04-13 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0008_remove_profile_email_remove_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='user',
            field=models.ForeignKey(default=48, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
