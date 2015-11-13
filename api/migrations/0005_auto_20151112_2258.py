# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151112_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightswitch',
            name='level',
            field=models.IntegerField(null=True),
        ),
    ]
