# Generated by Django 3.2 on 2021-07-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0013_alter_meeting_room_time_range_occupied'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_login',
            name='clas',
            field=models.CharField(default='', max_length=10, verbose_name='班级'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='direction',
            field=models.CharField(default='', max_length=45, verbose_name='专业方向'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='faculty',
            field=models.CharField(default='', max_length=100, verbose_name='院系'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='identity',
            field=models.CharField(default='', max_length=100, verbose_name='身份证'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='identity_class',
            field=models.CharField(default='', max_length=79, verbose_name='身份证件类型'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='major',
            field=models.CharField(default='', max_length=45, verbose_name='专业'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='phone_number',
            field=models.CharField(default='', max_length=78, verbose_name='手机号'),
        ),
        migrations.AddField(
            model_name='user_login',
            name='stu_job_number',
            field=models.CharField(default='', max_length=40, verbose_name='学号/工号'),
        ),
    ]
