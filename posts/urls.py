from django.urls import path

#from . import views
from .views import MfoView, PostDetails, Redirect
urlpatterns = [
    path('', MfoView , name='home'),
    path('мфо/<str:slug>', PostDetails.as_view(), name='post-details'),
    path('go/<str:slug>', Redirect.as_view(), name='redirect_go')
]
