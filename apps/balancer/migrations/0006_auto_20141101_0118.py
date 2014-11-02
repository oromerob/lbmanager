# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balancer', '0005_director_dirtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='dirtype',
            field=models.CharField(max_length=200, choices=[(b'Random', ((b'random', b'Random'), (b'client', b'Client'), (b'hash', b'Hash'))), (b'round-robin', b'Round Robin'), (b'dns', b'DNS'), (b'fallback', b'Fallback')]),
            preserve_default=True,
        ),
    ]