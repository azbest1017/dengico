# Generated by Django 3.1.4 on 2020-12-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20201206_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='percent_per_day',
            field=models.IntegerField(default=0),
        ),
    ]
