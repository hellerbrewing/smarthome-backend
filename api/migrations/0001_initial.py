# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garageopener',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('open', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lightscene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('on', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lightswitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('on', models.BooleanField(default=False)),
                ('level', models.IntegerField(verbose_name=models.Model)),
            ],
        ),
        migrations.CreateModel(
            name='Thermostat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('tempset', models.IntegerField(verbose_name=models.Model)),
                ('tempactual', models.IntegerField()),
                ('hold', models.BooleanField(default=False)),
                ('heat', models.BooleanField(default=False)),
            ],
        ),
    ]
