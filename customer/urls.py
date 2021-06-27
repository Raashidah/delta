
from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.one,name='home'),
    path('main',views.main,name='main'),
    path('signup',views.two,name='signup'),
    path('user',views.three,name='user'),
    path('pro',views.four,name='pro'),
    path('service',views.five,name='service'),
    path('offer',views.daily,name='offer'),
    path('view',views.viewproduct,name='view'),
    path('buy',views.buyproduct,name='buy'),
    path('address',views.addAddress,name='address'),
    path('paymode',views.paymethod,name='paymode'),
    path('placeorder',views.placeorder,name='placeorder'),
   
    
]
