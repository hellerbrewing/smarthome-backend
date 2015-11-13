# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightswitch',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='thermostat',
            name='tempset',
            field=models.IntegerField(),
        ),
    ]
