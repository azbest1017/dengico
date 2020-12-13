# Generated by Django 3.1.4 on 2020-12-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='first_credit_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='logo',
            field=models.TextField(default='0', max_length=240),
        ),
        migrations.AddField(
            model_name='post',
            name='max_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='max_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='min_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='min_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='Название', max_length=240, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='pament',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='scope',
            field=models.IntegerField(default=100),
        ),
    ]
