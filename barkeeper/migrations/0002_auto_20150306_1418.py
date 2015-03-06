# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterial',
            name='pump',
            field=models.OneToOneField(null=True, blank=True, to='barkeeper.Pump'),
            preserve_default=True,
        ),
    ]
