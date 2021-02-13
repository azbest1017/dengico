from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Affiliate_Partner(models.Model):
    name = models.CharField(max_length=300)
    api_key = models.CharField(max_length=500, default="api_key")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=160)

    def __str__(self):
        return self.name

class Methot_Withdraw(models.Model):
    name = models.CharField(max_length=160, unique=True)
    logo = models.ImageField(upload_to='static/images/withdraw/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    offer_status = models.BooleanField(verbose_name='Оффер включен', default=True)
    offer_want = models.BooleanField(verbose_name='Оффер в Проверке', default=True)
    offer_id = models.IntegerField(verbose_name='ID Оффера',default=0)
    category = models.ManyToManyField(Category,verbose_name='Категории')
    link = models.CharField(verbose_name='Ссылка партнерки',default="Ссылка", max_length=5000)
    name = models.CharField(verbose_name='Название МФО',max_length=240, unique=True, default="Название Оффера")
    logo = models.ImageField(verbose_name='Логотип',upload_to='static/images/mfo/', height_field=None, width_field=None, max_length=100)
    max_credit = models.IntegerField(verbose_name='Максимальный Займ',default=0)
    min_credit = models.IntegerField(verbose_name='Минимальный Займ',default=0)
    min_days = models.IntegerField(verbose_name='Минимальное количество дней',default=0)
    max_days = models.IntegerField(verbose_name='Максимальное количество дней',default=0)
    pament = models.IntegerField(verbose_name='Вознаграждение',default=0)
    scope = models.IntegerField(verbose_name='Рейтинг',default=100)
    first_credit_free = models.BooleanField(verbose_name='Первый Займ Бесплатно',default=False)
    percent_per_day = models.FloatField(verbose_name='Минимальный процент в день',default=0.0)
    keywords = models.CharField(verbose_name='Ключевые слова для СЕО',max_length=240, default=" ")
    description = models.CharField(verbose_name='Описание для СЕО',max_length=240, default="Описание для СЕО")
    body = models.TextField(verbose_name='Подробная Информация',max_length=5000, default="Описание")
    slug = models.SlugField(verbose_name='Название МФО',allow_unicode=True, unique=True) # new
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    partner = models.ManyToManyField(Affiliate_Partner,verbose_name='Партнерка')
    withdraw = models.ManyToManyField(Methot_Withdraw, verbose_name='Способы Вывода Займа')

    def __str__(self):
        return self.name + ' | ' + str(self.author)
