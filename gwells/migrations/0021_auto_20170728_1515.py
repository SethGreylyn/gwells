# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-28 22:15
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0020_auto_20170728_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='internal_diameter',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='Diameter'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='slot_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Slot Size'),
        ),
    ]
