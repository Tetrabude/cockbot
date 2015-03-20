# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0002_auto_20150306_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='pump',
            name='gpioId',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
