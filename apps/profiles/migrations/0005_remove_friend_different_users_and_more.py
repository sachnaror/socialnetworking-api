# Generated by Django 4.2.3 on 2023-09-11 15:11

from django.db import migrations, models
import django.db.models.functions.comparison


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0004_remove_friend_unique_user_combination_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="friend",
            name="different_users",
        ),
        migrations.RemoveConstraint(
            model_name="friend",
            name="unique_user_combination",
        ),
        migrations.AddConstraint(
            model_name="friend",
            constraint=models.UniqueConstraint(
                django.db.models.functions.comparison.Least("requester", "requestee"),
                django.db.models.functions.comparison.Greatest(
                    "requester", "requestee"
                ),
                name="bidirectional_unique_user_combination",
                violation_error_message="Friend with similar users already exists",
            ),
        ),
        migrations.AddConstraint(
            model_name="friend",
            constraint=models.CheckConstraint(
                check=models.Q(("requester", models.F("requestee")), _negated=True),
                name="different_users",
                violation_error_message="Requester and Requestee cannot be the same",
            ),
        ),
    ]
