from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def adminHome(request):
    return render(request,'adminmaster.html')
def adminProfile(request):
    return render(request,'adminprofile.html')
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