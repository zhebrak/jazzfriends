# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_type', models.SmallIntegerField(verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', choices=[(0, '\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')])),
                ('name', models.CharField(max_length=50, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('file', models.FileField(upload_to=b'/attachments/', verbose_name='\u0444\u0430\u0439\u043b')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('location', models.CharField(max_length=200, verbose_name='\u043c\u0435\u0441\u0442\u043e')),
                ('show_time', models.DateTimeField(verbose_name='\u0432\u0440\u0435\u043c\u044f')),
                ('site', models.URLField(null=True, verbose_name='\u0441\u0430\u0439\u0442', blank=True)),
                ('description', models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'ordering': ('-show_time',),
                'verbose_name': '\u041a\u043e\u043d\u0446\u0435\u0440\u0442',
                'verbose_name_plural': '\u041a\u043e\u043d\u0446\u0435\u0440\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u0438\u043c\u044f')),
                ('contact', models.CharField(max_length=100, verbose_name='\u043a\u043e\u043d\u0442\u0430\u043a\u0442')),
                ('message', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c',
                'verbose_name_plural': '\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c',
            },
        ),
    ]
