# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='ssl_port',
            field=models.IntegerField(default=443),
            preserve_default=True,
        ),
    ]