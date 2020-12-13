from django.urls import path

#from . import views
from .views import HomeView, PostDetails, Redirect
urlpatterns = [
    #path('', views.home, name="home"),
    path('',HomeView.as_view(), name="home"),
    path('мфо/<str:slug>', PostDetails.as_view(), name='post-details'),
    path('go/<str:slug>', Redirect.as_view(), name='redirect_go')
]
