# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20151122_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightswitch',
            name='devceID',
            field=models.IntegerField(unique=True, null=True),
        ),
    ]
