from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ahome(request):
    return render(request,'ahome.html')
def adminHome(request):
    return render(request,'adminmaster.html')
def deal(request):
    return render(request,'dealoftheday.html')
def adddeal(request):
    return render(request,'adddeal.html')    
def addProduct(request):
    return render(request,'addproduct.html')
def brand(request):
    return render(request,'brand.html')
def addBrand(request):
    return render(request,'addbrand.html')
def categories(request):
    return render(request,'categories.html')
def addItem(request):
    return render(request,'additem.html')
def addImage(request):
    return render(request,'addimage.html')
