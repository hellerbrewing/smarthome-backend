# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20151124_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lightscene',
            name='lightswitches',
        ),
        migrations.AddField(
            model_name='lightscene',
            name='sceneID',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lightswitch',
            name='deviceID',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lightswitch',
            name='level',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
