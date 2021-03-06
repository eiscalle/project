# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('message', models.TextField(default='', max_length=2000, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('email', models.EmailField(default='', max_length=255, verbose_name='E-mail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
        ),
        migrations.CreateModel(
            name='WantedSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0438\u0430\u043b\u0430')),
                ('season', models.PositiveSmallIntegerField(default=1, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0435\u0437\u043e\u043d\u0430')),
                ('language', models.CharField(choices=[('en', '\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439'), ('ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), ('ch', '\u041a\u0438\u0442\u0430\u0439\u0441\u043a\u0438\u0439')], default='en', max_length=24, verbose_name='\u042f\u0437\u044b\u043a \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0430')),
                ('email', models.EmailField(default='', max_length=255, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437 \u0441\u0435\u0440\u0438\u0430\u043b\u0430',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b \u0441\u0435\u0440\u0438\u0430\u043b\u043e\u0432',
            },
        ),
    ]
