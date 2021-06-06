
from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.one,name='home'),
    path('signup',views.two,name='signup'),
    path('user',views.three,name='user'),
    path('pro',views.four,name='pro'),
    path('service',views.five,name='service'),
    path('offer',views.daily,name='offer'),
    
    
]
