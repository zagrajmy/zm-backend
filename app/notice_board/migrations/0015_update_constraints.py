# Generated by Django 3.1 on 2020-08-18 16:44

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notice_board", "0014_alter_json_fields"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="meeting", name="meeting_unique_slug_in_guild",
        ),
        migrations.RemoveConstraint(
            model_name="meeting", name="meeting_unique_slug_in_sphere",
        ),
        migrations.RemoveConstraint(model_name="meeting", name="meeting_date_times",),
        migrations.AddConstraint(
            model_name="meeting",
            constraint=models.UniqueConstraint(
                fields=("slug", "sphere"), name="meeting_unique_slug_in_sphere"
            ),
        ),
        migrations.AddConstraint(
            model_name="meeting",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("end_time__isnull", True),
                        ("publication_time__isnull", True),
                        ("start_time__isnull", True),
                    ),
                    models.Q(
                        (
                            "publication_time__lte",
                            django.db.models.expressions.F("start_time"),
                        ),
                        ("start_time__lt", django.db.models.expressions.F("end_time")),
                    ),
                    _connector="OR",
                ),
                name="meeting_date_times",
            ),
        ),
    ]
