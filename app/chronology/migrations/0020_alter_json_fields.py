# Generated by Django 3.1 on 2020-08-11 18:00

from django.db import migrations, models

import chronology.models


class Migration(migrations.Migration):

    dependencies = [
        ("chronology", "0019_add_end_proposal_to_festival"),
    ]

    operations = [
        migrations.AlterField(
            model_name="festival",
            name="settings",
            field=models.JSONField(
                default=chronology.models.default_festival_settings,
                verbose_name="settings",
            ),
        ),
        migrations.AlterField(
            model_name="historicalfestival",
            name="settings",
            field=models.JSONField(
                default=chronology.models.default_festival_settings,
                verbose_name="settings",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="other_contact",
            field=models.JSONField(
                blank=True,
                default=chronology.models.default_json_field,
                verbose_name="other contact",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="other_data",
            field=models.JSONField(
                blank=True,
                default=chronology.models.default_json_field,
                verbose_name="other data",
            ),
        ),
    ]
