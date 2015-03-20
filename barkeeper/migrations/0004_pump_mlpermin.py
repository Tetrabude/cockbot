# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0003_pump_gpioid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pump',
            name='mlPerMin',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
