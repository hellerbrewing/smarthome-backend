# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20151127_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lightscene',
            old_name='sceneID',
            new_name='sceneIDoff',
        ),
        migrations.AddField(
            model_name='lightscene',
            name='sceneIDon',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
