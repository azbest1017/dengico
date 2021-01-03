from django.shortcuts import render
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView
from .models import Post, Methot_Withdraw
from django.contrib import messages
import requests, json

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
    first_credit_free = request.GET.get('first_credit_free')
    rubles = request.GET.get('rubles')
    weeks = request.GET.get('weeks')
    print(Post.objects.first().name)
    all_method_pay = []
    if first_credit_free == 'on':
        all_mfo = all_mfo.filter(first_credit_free=True)
    if is_it_valid(rubles):
        all_mfo = all_mfo.filter(max_credit__gte=rubles)
    if is_it_valid(weeks):
        weeks = int(weeks)*7
        all_mfo = all_mfo.filter(max_days__gte=weeks)
    all_withdraw = Methot_Withdraw.objects.all()
    for i in all_withdraw:
        d = i.name
        z = request.GET.get(d)
        x = i.pk
        if z == 'on':
            all_method_pay += [x]
    all_mfo = all_mfo.filter(withdraw__in=all_method_pay).distinct()
    if all_mfo.exists() == False:
        all_mfo = Post.objects.all()
        all_mfo = all_mfo.filter(offer_status=True)
        if is_it_valid(rubles):
            messages.error(request, "not_find", extra_tags='not_find')
    else:
        quantity = len(all_mfo)
        if is_it_valid(rubles):
            messages.success(request, str(quantity), extra_tags='find')
    return all_mfo


def MfoView(request):
    all_mfo = filter(request)
    context = {
        'posts': all_mfo.order_by('-pament','-scope'),
        'methods': Methot_Withdraw.objects.all(),
}
    return render(request, "home.html", context)
