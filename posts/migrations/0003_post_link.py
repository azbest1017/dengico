# Generated by Django 3.1.4 on 2020-12-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201205_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='Ссылка', max_length=5000),
        ),
    ]