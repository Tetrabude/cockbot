# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0008_auto_20150327_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawmaterial',
            name='pump',
        ),
        migrations.AddField(
            model_name='pump',
            name='rawMaterial',
            field=models.ForeignKey(null=True, blank=True, to='barkeeper.RawMaterial'),
            preserve_default=True,
        ),
    ]
