from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def one(request):
    return render(request,'home.html')
def two(request):
    return render(request,'signup.html')
def three(request):
    return render(request,'usermaster.html')
def four(request):
    return render(request,'profile.html')
def five(request):
    return render(request,'service.html') 
def daily(request):
    return render(request,'dailyoffer.html')   