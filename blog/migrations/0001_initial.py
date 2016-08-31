# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('제목', models.CharField(max_length=200)),
                ('내용', models.TextField()),
                ('작성시간', models.DateTimeField(default=django.utils.timezone.now)),
                ('배포시간', models.DateTimeField(blank=True, null=True)),
                ('작성자', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
