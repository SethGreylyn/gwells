# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0007_auto_20170629_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lithologydescription',
            name='water_bearing_estimated_flow',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Water Bearing Estimated Flow'),
        ),
    ]
