# Generated by Django 3.2 on 2021-06-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0011_alter_user_login_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='xueyu',
            name='direction',
            field=models.CharField(default='无', max_length=100, verbose_name='研究方向'),
        ),
    ]