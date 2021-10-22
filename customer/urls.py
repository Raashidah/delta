from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('log/',views.log,name='login'),
    path('main',views.main,name='main'),
    # path('signup',views.two,name='signup'),
    path('user',views.three,name='user'),
    path('viewpro/',views.profile,name='viewpro'),
    path('pro/<int:id>',views.viewprofile,name='pro'),
    path('update/<int:id>',views.updatedata,name='update'),
    path('service',views.five,name='service'),
    path('offer',views.daily,name='offer'),
    path('view/',views.viewproduct,name='view'),
    path('buy',views.buyproduct,name='buy'),
    path('address',views.addAddress,name='address'),
    path('paymode',views.paymethod,name='paymode'),
    path('placeorder',views.placeorder,name='placeorder'),
   
    
]
