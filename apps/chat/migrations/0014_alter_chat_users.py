# Generated by Django 4.2.3 on 2024-09-16 21:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0013_remove_chat_dm_chat_constraints_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
