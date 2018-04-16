# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('rank', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, null=True)),
                ('url', models.URLField(null=True)),
                ('image_url', models.URLField(null=True)),
                ('summary', models.TextField(null=True)),
                ('best_movie', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
