# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0013_auto_20170724_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurfaceSealType',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('surface_seal_type_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_surface_seal_type',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.RemoveField(
            model_name='activitysubmission',
            name='surface_seal_material',
        ),
        migrations.RemoveField(
            model_name='well',
            name='surface_seal_material',
        ),
        migrations.DeleteModel(
            name='SurfaceSealMaterial',
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='surface_seal_type',
            field=models.ForeignKey(blank=True, db_column='surface_seal_type_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.SurfaceSealType', verbose_name='Surface Seal Type'),
        ),
        migrations.AddField(
            model_name='well',
            name='surface_seal_type',
            field=models.ForeignKey(blank=True, db_column='surface_seal_type_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.SurfaceSealType', verbose_name='Surface Seal Type'),
        ),
    ]
