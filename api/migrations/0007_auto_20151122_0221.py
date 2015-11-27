# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smarthome.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151122_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garageopener',
            name='name',
            field=models.CharField(unique=True, max_length=20, validators=[smarthome.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='lightscene',
            name='name',
            field=models.CharField(unique=True, max_length=20, validators=[smarthome.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='thermostat',
            name='name',
            field=models.CharField(unique=True, max_length=20, validators=[smarthome.api.validators.removeJavascriptKeyword]),
        ),
    ]
