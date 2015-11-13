# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_lightscene_lightswitches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightswitch',
            name='level',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
