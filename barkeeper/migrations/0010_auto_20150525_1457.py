# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0009_auto_20150523_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.URLField(null=True, default='', blank=True, max_length=256),
            preserve_default=True,
        ),
    ]
