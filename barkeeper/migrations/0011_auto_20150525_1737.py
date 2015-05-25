# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0010_auto_20150525_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='', max_length=2048, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instruction',
            field=models.TextField(default='', max_length=2048, blank=True, null=True),
            preserve_default=True,
        ),
    ]
