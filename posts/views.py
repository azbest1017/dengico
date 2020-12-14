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

def filter(request):
    all_mfo = Post.objects.all()
    first_credit_free = request.GET.get('first_credit_free')
    if first_credit_free == 'on':
        all_mfo = all_mfo.filter(first_credit_free=True)
        print(all_mfo)
    return all_mfo

def MfoView(request):
    all_mfo = filter(request)
    context = {
        'posts': all_mfo.order_by('-pament','-scope')
    }
    return render(request, "home.html", context)
