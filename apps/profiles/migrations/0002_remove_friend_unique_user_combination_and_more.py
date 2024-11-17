# Generated by Django 4.2.3 on 2024-09-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="friend",
            name="unique_user_combination",
        ),
        migrations.AddConstraint(
            model_name="friend",
            constraint=models.UniqueConstraint(
                models.OrderBy(models.F("requester"), models.F("requestee")),
                name="unique_user_combination",
            ),
        ),
    ]
