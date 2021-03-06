# Generated by Django 3.0.8 on 2020-07-21 18:09

from django.db import migrations


def make_char_fields_blank(apps, schema_editor):
    Meeting = apps.get_model("notice_board", "Meeting")

    Meeting.objects.filter(location=None).update(location="")


def make_char_fields_null(apps, schema_editor):
    Meeting = apps.get_model("chronology", "Meeting")

    Meeting.objects.filter(location="").update(location=None)


class Migration(migrations.Migration):

    dependencies = [
        ("notice_board", "0009_locale"),
    ]

    operations = [migrations.RunPython(make_char_fields_blank, make_char_fields_null)]
