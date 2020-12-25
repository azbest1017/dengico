from django.shortcuts import render
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView
from .models import Post, Methot_Withdraw
import requests, json ,schedule, time, datetime

#def home(request):
#    return render(request, 'home.html', {})
#class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
    # ordering = ['-pament','-scope']

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
    all_method_pay = request.POST.getlist('all_method_pay[]')
    if first_credit_free == 'on':
        all_mfo = all_mfo.filter(first_credit_free=True)
        print(all_mfo)
    if is_it_valid(rubles):
        all_mfo = all_mfo.filter(max_credit__gte=rubles)
    if is_it_valid(weeks):
        weeks = int(weeks)*7
        all_mfo = all_mfo.filter(max_days__gte=weeks)
    all_withdraw = Methot_Withdraw.objects.all()
    print(all_method_pay)

    return all_mfo


def MfoView(request):
    all_mfo = filter(request)
    context = {
        'posts': all_mfo.order_by('-pament','-scope'),
        'methods': Methot_Withdraw.objects.all()
}
    return render(request, "home.html", context)
