# Generated by Django 4.2.3 on 2024-10-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0015_remove_notification_selected_object_constraints_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="text",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
