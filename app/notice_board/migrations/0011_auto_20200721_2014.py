# Generated by Django 3.0.8 on 2020-07-21 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_update_default_site'),
        ('notice_board', '0010_blank_charfields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notice_board.Guild', verbose_name='guild'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.TextField(blank=True, default='', verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='publication_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='publication time'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start time'),
        ),
        migrations.AlterField(
            model_name='sphere',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='sphere', to='sites.Site', verbose_name='site'),
        ),
    ]
