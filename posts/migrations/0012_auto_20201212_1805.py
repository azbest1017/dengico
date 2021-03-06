# Generated by Django 3.1.4 on 2020-12-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20201212_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliate_Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(verbose_name=range(1, 10))),
                ('comment', models.TextField(max_length=160)),
                ('name', models.CharField(max_length=160)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='partner',
            field=models.ManyToManyField(to='posts.Affiliate_Partner'),
        ),
    ]
