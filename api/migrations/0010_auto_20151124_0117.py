# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20151124_0111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lightswitch',
            old_name='devceid',
            new_name='deviceID',
        ),
    ]
