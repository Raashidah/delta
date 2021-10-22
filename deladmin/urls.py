from django.urls import path,include
from . import views

urlpatterns = [
    path('ahome/',views.ahome,name='ahome'),
    path('signUP/',views.sign,name='sign'),
    path('dhome/',views.adminHome,name='dhome'),
    path('addbrand/',views.addBrand,name='addbrand'),
    path('brand/',views.brands,name='brand'),
    path('delbrand/<int:id>',views.deletebrand,name='delbrand'),
    path('cat/',views.categories,name='cat'),
    path('editcat/<int:id>',views.editcat,name='editcat'),
    
    path('addcate/',views.addcate,name='additem'),
    path('updatecat/<int:id>',views.updatecate,name='update'),
    path('delcate/<int:id>',views.deletecate,name='delcate'),
    path('changecato/',views.changecato,name='changecato'),
    
    path('changepro/',views.changepro,name='changepro'),
    path('changeprod/',views.changeprod,name='changeprod'),
    

    path('deal',views.deal,name='deal'),
    path('adddeal',views.adddeal,name='adddeal'),
    path('product/',views.addProduct,name='product'),
    path('image/',views.addImage,name='image'),
    path('viewprod/',views.viewProduct,name='viewprod'),
    path('editpro/<int:id>',views.editproduct,name='editpro'),
    path('updatepro/<int:id>',views.updateprod,name='updatepro'),
    
   
    
    
    
]