# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-02 21:44
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0021_auto_20170728_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopmentMethod',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('development_method_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_development_method',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='development_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Development Total Duration'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='development_notes',
            field=models.CharField(blank=True, max_length=255, verbose_name='Development Notes'),
        ),
        migrations.AddField(
            model_name='well',
            name='development_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Development Total Duration'),
        ),
        migrations.AddField(
            model_name='well',
            name='development_notes',
            field=models.CharField(blank=True, max_length=255, verbose_name='Development Notes'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='other_screen_bottom',
            field=models.CharField(blank=True, max_length=50, verbose_name='Specify Other Screen Bottom'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='other_screen_material',
            field=models.CharField(blank=True, max_length=50, verbose_name='Specify Other Screen Material'),
        ),
        migrations.AlterField(
            model_name='well',
            name='other_screen_bottom',
            field=models.CharField(blank=True, max_length=50, verbose_name='Specify Other Screen Bottom'),
        ),
        migrations.AlterField(
            model_name='well',
            name='other_screen_material',
            field=models.CharField(blank=True, max_length=50, verbose_name='Specify Other Screen Material'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='development_method',
            field=models.ForeignKey(blank=True, db_column='development_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.DevelopmentMethod', verbose_name='Development Method'),
        ),
        migrations.AddField(
            model_name='well',
            name='development_method',
            field=models.ForeignKey(blank=True, db_column='development_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.DevelopmentMethod', verbose_name='Development Method'),
        ),
    ]
