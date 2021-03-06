# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-06 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(verbose_name='预定日期')),
                ('booking_time', models.IntegerField(choices=[(1, '8:30 - 9:00'), (2, '9:00 - 9:30'), (3, '9:30 - 10:00'), (4, '10:00 - 10:30'), (5, '10:30 - 11:00'), (6, '11:00 - 11:30'), (7, '11:30 - 12:00'), (8, '12:00 - 12:30'), (9, '12:30 - 13:00'), (10, '13:00 - 13:30'), (11, '13:30 - 14:00'), (12, '14:00 - 14:30'), (13, '14:30 - 15:00'), (14, '15:00 - 15:30'), (15, '15:30 - 16:00'), (16, '16:00 - 16:30'), (17, '16:30 - 17:00'), (18, '17:00 - 17:30'), (19, '17:30 - 18:00'), (20, '18:00 - 18:30'), (21, '18:30 - 19:00'), (22, '19:00 - 19:30'), (23, '19:30 - 20:00'), (24, '20:00 - 20:30')], verbose_name='预定时间段')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='会议室')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.MeetingRoom', verbose_name='会议室'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo', verbose_name='用户'),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set([('booking_date', 'booking_time')]),
        ),
    ]
