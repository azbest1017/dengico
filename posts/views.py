from django.shortcuts import render
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView
from .models import Post, Methot_Withdraw
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
    first_credit_free = request.GET.get('first_credit_free')
    rubles = request.GET.get('rubles')
    weeks = request.GET.get('weeks')
    if first_credit_free == 'on':
        all_mfo = all_mfo.filter(first_credit_free=True)
        print(all_mfo)
    if is_it_valid(rubles):
        all_mfo = all_mfo.filter(max_credit__gte=rubles)
    if is_it_valid(weeks):
        weeks = int(weeks)*7
        all_mfo = all_mfo.filter(max_days__gte=weeks)
        print(weeks)
    return all_mfo

def MfoView(request):
    all_mfo = filter(request)
    context = {
        'posts': all_mfo.order_by('-pament','-scope')
    }
    return render(request, "home.html", context)
