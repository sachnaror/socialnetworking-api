# Generated by Django 4.2.3 on 2024-09-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0003_remove_chat_dm_chat_constraints_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="chat",
            name="dm_chat_constraints",
        ),
        migrations.AddConstraint(
            model_name="chat",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("ctype", "DM"),
                    ("name", None),
                    ("description", None),
                    ("image", None),
                ),
                name="dm_chat_constraints",
            ),
        ),
    ]
