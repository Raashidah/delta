from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class signup(models.Model):
    email=models.EmailField(max_length=50)
class adminLogin(models.Model):
    admin_id=models.ForeignKey(signup,on_delete=CASCADE)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class brand(models.Model):
    brand_name=models.CharField(max_length=30)
class category(models.Model):
    category=models.CharField(max_length=30)
    brand=models.ForeignKey(brand,on_delete=CASCADE)
class product(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    # color=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
    # size=models.CharField(max_length=10)
    discount=models.CharField(max_length=5)
    brand=models.ForeignKey(brand,on_delete=CASCADE)
    category=models.ForeignKey(category,on_delete=CASCADE)
class image(models.Model):
    # brand=models.ForeignKey(brand,on_delete=CASCADE)
    # category=models.ForeignKey(category,on_delete=CASCADE)   
    product=models.ForeignKey(product,on_delete=CASCADE) 
    image=models.CharField(max_length=300)  


    