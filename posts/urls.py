from django.urls import path

#from . import views
from .views import MfoView,PostDetails,Redirect,Online,Free,Na_kartu,Na_schet,Na_qiwi,Na_yandex,Na_mir,Na_nal,Na_contact,Na_corona,Bez_karti,Kruglo,Bez_proverki,Bez_pas,Bez_otkaz,Srochno
urlpatterns = [
    path('', MfoView , name='home'),
    path('Онлайн-Займ', Online , name='Online'),
    path('Бесплатный-Займ', Free , name='Free'),
    path('Займ-на-Карту', Na_kartu , name='Na_kartu'),
    path('Займ-на-Счет', Na_schet , name='Na_schet'),
    path('Займ-на-Киви', Na_qiwi , name='Na_qiwi'),
    path('Займ-на-Яндекс-Деньги', Na_yandex, name='Na_yandex'),
    path('Займ-на-Карту-Мир', Na_mir, name='Na_mir'),
    path('Займ-Наличными', Na_nal, name='Na_nal'),
    path('Займ-Переводом-Contact', Na_contact, name='Na_contact'),
    path('Займ-Переводом-Золотая-Корона', Na_corona, name='Na_corona'),
    path('Займ-Без-Карты', Bez_karti, name='Bez_karti'),
    path('Займ-Круглосуточно', Kruglo, name='Kruglo'),
    path('Займ-без-Проверки', Bez_proverki, name='Bez_proverki'),
    path('Займ-без-Паспорта', Bez_pas, name='Bez_pas'),
    path('Займ-без-Отказа-и-Проверок', Bez_otkaz, name='Bez_otkaz'),
    path('Займ-Срочно', Srochno, name='Srochno'),
    path('мфо/<str:slug>', PostDetails.as_view(), name='post-details'),
    path('go/<str:slug>', Redirect.as_view(), name='redirect_go')
]
