# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smarthome.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151112_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightswitch',
            name='name',
            field=models.CharField(unique=True, max_length=20, validators=[smarthome.api.validators.removeJavascriptKeyword]),
        ),
    ]
