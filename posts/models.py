from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Affiliate_Partner(models.Model):
    name = models.CharField(max_length=300)
    api_key = models.CharField(max_length=500, default="api_key")
    account = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    stars = models.IntegerField(range(1,10))
    comment = models.TextField(max_length=160)
    name = models.CharField(max_length=160)

    def __str__(self):
        return self.stars  + ' | ' + self.name

class Methot_Withdraw(models.Model):
    name = models.CharField(max_length=160, unique=True)
    logo = models.ImageField(upload_to='static/images/withdraw/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    link = models.CharField(default="Ссылка партнерки", max_length=5000)
    name = models.CharField(max_length=240, unique=True, default="Название Оффера")
    logo = models.ImageField(upload_to='static/images/mfo/', height_field=None, width_field=None, max_length=100)
    max_credit = models.IntegerField(default=0)
    min_credit = models.IntegerField(default=0)
    min_days = models.IntegerField(default=0)
    max_days = models.IntegerField(default=0)
    pament = models.IntegerField(default=0)
    scope = models.IntegerField(default=100)
    first_credit_free = models.BooleanField(default=False)
    percent_per_day = models.FloatField(default=0.0)
    keywords = models.CharField(max_length=240, default="Ключевые слова для СЕО")
    description = models.CharField(max_length=240, default="Описание для СЕО")
    body = models.TextField(max_length=5000, default="Описание")
    slug = models.SlugField(allow_unicode=True, unique=True) # new
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    partner = models.ManyToManyField(Affiliate_Partner)
    withdraw = models.ManyToManyField(Methot_Withdraw)

    def __str__(self):
        return self.name + ' | ' + str(self.author)
