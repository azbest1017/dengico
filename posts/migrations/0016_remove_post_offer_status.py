# Generated by Django 3.1.4 on 2020-12-22 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20201222_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='offer_status',
        ),
    ]
