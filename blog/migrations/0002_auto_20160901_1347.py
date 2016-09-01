# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='작성자',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='작성시간',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='배포시간',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='내용',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='제목',
            new_name='title',
        ),
    ]
