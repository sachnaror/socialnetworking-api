# Generated by Django 4.2.3 on 2024-10-04 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("profiles", "0011_alter_notification_read_by_alter_notification_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="receivers",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name="notification",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("comment", None), ("post__isnull", False), ("reply", None)
                    ),
                    models.Q(
                        ("comment__isnull", False), ("post", None), ("reply", None)
                    ),
                    models.Q(
                        ("comment", None), ("post", None), ("reply__isnull", False)
                    ),
                    models.Q(("comment", None), ("post", None), ("reply", None)),
                    _connector="OR",
                ),
                name="selected_object_constraints",
                violation_error_message="Cannot have cannot have post, comment, reply or any two of the three simultaneously",
            ),
        ),
        migrations.AddConstraint(
            model_name="notification",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("ntype", "ADMIN"), ("sender", None), ("text__isnull", False)
                    ),
                    models.Q(
                        models.Q(("ntype", "ADMIN"), _negated=True),
                        ("sender__isnull", False),
                        ("text", None),
                    ),
                    _connector="OR",
                ),
                name="sender_text_type_constraints",
                violation_error_message="\n                    If Sender, type must be ADMIN and text musn't be None and vice versa.\n                ",
            ),
        ),
    ]
