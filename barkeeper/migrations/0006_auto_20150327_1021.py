# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0005_auto_20150327_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=b'', max_length=2048),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instruction',
            field=models.TextField(default=b'', max_length=2048),
            preserve_default=True,
        ),
    ]
