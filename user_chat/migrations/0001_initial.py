# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-03 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
