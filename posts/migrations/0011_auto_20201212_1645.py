# Generated by Django 3.1.4 on 2020-12-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20201212_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(upload_to='static/images/mfo/'),
        ),
    ]
