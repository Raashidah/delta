from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls.resolvers import LocaleRegexDescriptor
from . models import login,signup
from deladmin . models import * 

# Create your views here.
def home(request):
    try:
        mobile=request.POST['mn']
        userExist=login.objects.filter(mobile=mobile).exists()
        if userExist==False:
            Name=request.POST['firstname']
            Email=request.POST['email']
            Password=request.POST['pwd']
            house=request.POST['house']
            area=request.POST['area']
            city=request.POST['city']
            dist=request.POST['dist']
            state=request.POST['state']
            pin=request.POST['pin']
            Address=house+','+area+','+city+','+dist+','+state+','+pin
            
            signupObj=signup(name=Name,email=Email,address=Address)
            signupObj.save()
            loginObj=login(mobile=mobile,password=Password,customer_id_id=signupObj.id)
            loginObj.save()
            return render(request,'home.html',{"msg":"user saved" })
        else:
            return render(request,'home.html',{"msg":"User already exist!!!" })  
    except Exception as e:
        print(e)  
    return render(request,'home.html')      


    # return render(request,'home.html')


def log(request):
    try:
        mobile=request.POST['mobile']
        password=request.POST['password']
        user_log=login.objects.get(mobile=mobile,password=password)
        request.session['user']=user_log.id
        
        print(user_log.customer_id_id)
        user_obj1=signup.objects.get(id=user_log.customer_id_id)
        # print(user_obj1.Firstname)
        return render(request,'main.html',{"user":user_obj1})      
    except Exception as e:
        print(e)
        return render(request,'home.html',{"msg":"invalid username or password"})
    # return render(request,'home.html')
def three(request):
    return render(request,'usermaster.html')
def main(request):
    return render(request,'main.html')
def profile(request):
    session_data=request.session['user']
    profile=login.objects.get(id=session_data)
    signprofile=signup.objects.get(id=profile.customer_id_id)
    return render(request,'viewpro.html',{"profile":profile,"sprofile":signprofile})
    
def viewprofile(request,id):
    logindata=login.objects.get(id=id)
    signdata=signup.objects.get(id=id)
    return render(request,'profile.html',{"data":logindata,"datas":signdata})
    
def updatedata(request,id):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
        login.objects.filter(id=id).update(mobile=mobile,password=password)
        signup.objects.filter(id=id).update(name=name,email=email)
        return redirect('viewpro')   

def five(request):
    return render(request,'service.html') 
def daily(request):
    return render(request,'dailyoffer.html')   
def viewproduct(request):
    prod=image.objects.all()
    brands=product.objects.all()
    return render(request,'delpro.html',{"product":prod,"brand":brands})
def items(request,id): 
    pro=product.objects.get(id=id)
    prod=image.objects.filter(product_id=pro)
    for x in prod:
        mainimage=x.image
    return render(request,'items.html',{"prod":pro,"img":prod,"imge":mainimage})    
def buyproduct(request):
    return render(request,'buy.html')
def addAddress(request):
    return render(request,'address.html')
def paymethod(request):
    return render(request,'paymode.html')
def placeorder(request):
    return render(request,'placeorder.html')
