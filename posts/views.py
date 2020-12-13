from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Methot_Withdraw
#def home(request):
#    return render(request, 'home.html', {})
class HomeView(ListView):
     model = Post
     template_name = 'home.html'
     ordering = ['-pament','-scope']

class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'

class Redirect(DetailView):
    model = Post
    template_name = 'redirect.html'
    
