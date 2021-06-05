from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('dhome',views.adminHome,name='dhome'),
    path('deal',views.deal,name='deal'),
    path('adddeal',views.adddeal,name='adddeal'),
    path('product',views.addProduct,name='product'),
    path('brand',views.brand,name='brand'),
    path('addbrand',views.addBrand,name='addbrand'),
    path('items',views.categories,name='items'),
    path('additem',views.addItem,name='additem'),
]