# Generated by Django 3.1.2 on 2020-10-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20201023_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerfollowup',
            name='intention',
            field=models.SmallIntegerField(choices=[(0, '2周内报名'), (1, '1个月内报名'), (2, '近期无报名计划'), (3, '已在其它机构报名'), (4, '已报名'), (5, '已拉黑')], default=1),
            preserve_default=False,
        ),
    ]
