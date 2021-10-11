# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-10-10 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ipy_manager_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='network',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('network', models.GenericIPAddressField(protocol='IPv4')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('owner', models.TextField(max_length=30)),
                ('tag', models.TextField(max_length=10)),
                ('netmask', models.GenericIPAddressField(protocol='IPv4')),
            ],
        ),
        migrations.CreateModel(
            name='range',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('network', models.GenericIPAddressField(protocol='IPv4')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('owner', models.TextField(max_length=30)),
                ('tag', models.TextField(max_length=10)),
            ],
        ),
    ]
