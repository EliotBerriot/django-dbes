# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 17:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ('-creation_date',)},
        ),
    ]

