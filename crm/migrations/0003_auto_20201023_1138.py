# Generated by Django 3.1.2 on 2020-10-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20201023_1031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': '校区'},
        ),
        migrations.AlterModelOptions(
            name='classlist',
            options={'verbose_name_plural': '班级'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '课程'},
        ),
        migrations.AlterModelOptions(
            name='courserecord',
            options={'verbose_name_plural': '上课记录'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': '客户信息'},
        ),
        migrations.AlterModelOptions(
            name='customerfollowup',
            options={'verbose_name_plural': '客户跟进'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name_plural': '报名'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name_plural': '缴费记录'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name_plural': '角色'},
        ),
        migrations.AlterModelOptions(
            name='studyrecord',
            options={'verbose_name_plural': '学习记录'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': '账号'},
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='crm.Tag'),
        ),
    ]
