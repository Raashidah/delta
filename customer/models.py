from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
class login(models.Model):
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=15)    
    customer_id=models.ForeignKey(signup,on_delete=CASCADE)

