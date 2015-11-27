# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_lightswitch_devceid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lightswitch',
            old_name='devceID',
            new_name='devceid',
        ),
    ]
