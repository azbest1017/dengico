# Generated by Django 3.1.4 on 2020-12-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_remove_post_offer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='offer_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='offer_status',
            field=models.BooleanField(default=True),
        ),
    ]
