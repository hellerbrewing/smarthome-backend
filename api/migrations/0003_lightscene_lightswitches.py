# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151112_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightscene',
            name='lightswitches',
            field=models.ManyToManyField(related_name='lightswitches', to='api.Lightswitch'),
        ),
    ]
