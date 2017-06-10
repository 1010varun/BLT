# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-09 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20170606_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.PositiveSmallIntegerField(choices=[(1, b'Number Error'), (2, b'Functional'), (3, b'Performance'), (4, b'Security'), (5, b'Typo'), (6, b'Design'), (0, b'Unspecified')], default=0),
        ),
    ]
