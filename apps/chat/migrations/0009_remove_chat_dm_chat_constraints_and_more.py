# Generated by Django 4.2.3 on 2024-09-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0008_remove_chat_dm_chat_constraints_and_more"),
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
                    models.Q(
                        ("ctype", "DM"),
                        ("description", None),
                        ("image", None),
                        ("name", None),
                    ),
                    ("ctype", "GROUP"),
                    _connector="OR",
                ),
                name="dm_chat_constraints",
            ),
        ),
    ]
