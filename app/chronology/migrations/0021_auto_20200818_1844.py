# Generated by Django 3.1 on 2020-08-18 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notice_board", "0015_update_constraints"),
        ("chronology", "0020_alter_json_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agendaitem",
            name="meeting",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="agenda_item",
                to="notice_board.meeting",
                verbose_name="meeting",
            ),
        ),
        migrations.AlterField(
            model_name="agendaitem",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="agenda_item",
                to="chronology.room",
                verbose_name="room",
            ),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="meeting",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proposal",
                to="notice_board.meeting",
                verbose_name="meeting",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="festival",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rooms",
                to="chronology.festival",
                verbose_name="festival",
            ),
        ),
        migrations.AlterField(
            model_name="timeslot",
            name="festival",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="time_slots",
                to="chronology.festival",
                verbose_name="festival",
            ),
        ),
    ]
