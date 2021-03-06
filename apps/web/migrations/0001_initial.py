# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('balancer', '0001_initial'),
        ('nginx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('cache', models.BooleanField(default=True)),
                ('director', models.ForeignKey(to='balancer.Director')),
                ('virtual_host', models.ForeignKey(to='nginx.NginxVirtualHost')),
            ],
            options={
                'verbose_name': 'Domain',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DomainAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('domain', models.ForeignKey(to='web.Domain')),
            ],
            options={
                'verbose_name': 'Domain Alias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostRedir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('domain', models.ForeignKey(to='web.Domain')),
            ],
            options={
                'verbose_name': 'Host Redir',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UrlRedir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('virtual_host', models.ForeignKey(to='nginx.NginxVirtualHost')),
            ],
            options={
                'verbose_name': 'URL Redir',
            },
            bases=(models.Model,),
        ),
    ]
