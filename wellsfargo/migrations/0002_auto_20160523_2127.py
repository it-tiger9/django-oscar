# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wellsfargo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_requests', to=settings.AUTH_USER_MODEL, verbose_name='Requesting User'),
        ),
    ]
