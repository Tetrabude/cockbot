# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkeeper', '0004_pump_mlpermin'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='alcohol',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='instruction',
            field=models.CharField(default=b'', max_length=2048),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.URLField(default=b'', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(default=b'', max_length=2048),
            preserve_default=True,
        ),
    ]
