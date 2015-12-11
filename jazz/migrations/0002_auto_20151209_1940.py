# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('location', models.CharField(max_length=200, verbose_name='\u043c\u0435\u0441\u0442\u043e')),
                ('show_date', models.DateField(verbose_name='\u0434\u0430\u0442\u0430')),
                ('embed_link', models.CharField(max_length=100, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e')),
            ],
            options={
                'ordering': ('-show_date',),
                'verbose_name': '\u0412\u0438\u0434\u0435\u043e',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e',
            },
        ),
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to=b'attachments/', verbose_name='\u0444\u0430\u0439\u043b'),
        ),
    ]
