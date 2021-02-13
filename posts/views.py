from django.shortcuts import render
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView
from .models import Post, Methot_Withdraw
from django.contrib import messages
from django.core.paginator import Paginator

class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'

class Redirect(DetailView):
    model = Post
    template_name = 'redirect.html'

def is_it_valid(param):
    return param != '' and param is not None

def filter(request):
    all_mfo = Post.objects.all()
    all_mfo = all_mfo.filter(offer_status=True)
    rubles = request.GET.get('rubles')
    weeks = request.GET.get('weeks')
    if is_it_valid(rubles):
        all_mfo = all_mfo.filter(max_credit__gte=rubles)
    if is_it_valid(weeks):
        weeks = int(weeks)*7
        all_mfo = all_mfo.filter(max_days__gte=weeks)
    return all_mfo


def MfoView(request):
    all_mfo = filter(request)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Самые <strong>выгодные и быстрые займы</strong> по всей России. Доступно <strong> " + str(quantity) + " </strong> микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "home.html", context)

def Online(request):
    all_mfo = filter(request)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>онлайн займы</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Online.html", context)

def Free(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(first_credit_free=True)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(first_credit_free=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>бесплатные займы под 0%</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Free.html", context)

def Na_kartu(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы на банковскую карту </strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_kartu.html", context)

def Na_schet(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы на банковский счет </strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_schet.html", context)

def Na_qiwi(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы на Киви Кошелек </strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_qiwi.html", context)

def Na_yandex(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы на Яндекс Деньги(Yoomoney) </strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_yandex.html", context)

def Na_mir(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы на банковскую карту МИР</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_mir.html", context)

def Na_nal(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы наличными</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_nal.html", context)

def Na_contact(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы наличными, переводом через CONTACT</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_contact.html", context)

def Na_corona(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы наличными, через Золотая Корона</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Na_corona.html", context)

def Bez_karti(request):
    all_mfo = filter(request)
    all_mfo = all_mfo.filter(withdraw__in=['3','4'])
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        all_mfo = all_mfo.filter(withdraw__in=('3','4')).distinct()
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы без банковской карты</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Bez_karti.html", context)

def Kruglo(request):
    all_mfo = filter(request)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы круглосуточно 24/7</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Kruglo.html", context)

def Bez_proverki(request):
    all_mfo = filter(request)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы без проверки</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Bez_proverki.html", context)

def Bez_pas(request):
    all_mfo = filter(request)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы без паспорта</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Bez_pas.html", context)

def Bez_otkaz(request):
    all_mfo = filter(request)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>займы без отказа и проверок</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Bez_otkaz.html", context)

def Srochno(request):
    all_mfo = filter(request)
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.error(request, "<strong>Не найденно подходящего МФО</strong>. Попробуйте другие параметры поиска.", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        all_mfo = all_mfo.order_by('-scope')
        paginator = Paginator(all_mfo, 14)
        page = request.GET.get('page', 1)
        try:
        	all_mfo = paginator.page(page)
        except PageNotAnInteger:
            all_mfo = paginator.page(1)
        except EmptyPage:
            all_mfo = paginator.page(paginator.num_pages)
        messages.success(request, "Выгодные <strong>срочные займы</strong> в России. Найденно <strong> " + str(quantity) + " </strong> Микрофинансовых организаций", extra_tags='find')
    context = {
        'posts': all_mfo,
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "pages/Srochno.html", context)
