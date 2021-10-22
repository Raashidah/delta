from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from random import random
from django.http import HttpResponse 
from . models import adminLogin, category, image, product,signup,brand
from django.core.files.storage import FileSystemStorage
# Create your views here.

def sign(request):
    try:
        username=request.POST['name']
        userlogexist=adminLogin.objects.filter(username=username).exists()
        if userlogexist==False:
            email=request.POST['email']
            password=request.POST['pass']
            signobj=signup(email=email)
            signobj.save()
            # print(signobj.email)
            logobj=adminLogin(username=username,password=password,admin_id_id=signobj.id)
            logobj.save()
            return render(request,'sign.html',{"msg":"user saved"})
        else:
            return render(request,'sign.html',{"msg":"user already exist"})   
    except Exception as e:
        print(e)
    return render(request,'sign.html')         
def ahome(request):
    try:
        
        username=request.POST['username']
        password=request.POST['pass']

        log_obj=adminLogin.objects.get(username=username,password=password)
        request.session['admin']=log_obj.id
        # print(log_obj.admin_id_id)
        admin_obj1=signup.objects.get(id=log_obj.admin_id_id)
        return render(request,'dealoftheday.html',{"user":admin_obj1})

        return render(request,'ahome.html',{"msg":"invalid username or password"})    
        
    except Exception as e:
        print(e)
        return render(request,'ahome.html')

    # return render(request,'ahome.html')
def adminHome(request):
    return render(request,'adminmaster.html')

def addBrand(request):
    try:
        brandname=request.POST['brand']
        brandexist=brand.objects.filter(brand_name=brandname).exists()
        if brandexist == False:
            aobj=brand(brand_name=brandname) 
            aobj.save()
            # print(aobj.brand)
            return render(request,'addbrand.html',{"msg1":"added successfully"})
        else:
            return render(request,'addbrand.html',{"msg1":"already exist"})                    
    except Exception as e:
        print(e)
    return render(request,'addbrand.html')
def brands(request):
    br=brand.objects.all()
    return render(request,'brand.html',{"br":br}) 
def deletebrand(request,id):
    brand.objects.get(id=id).delete()
    return redirect('brand')   


def addcate(request): 
    try: 
        br=brand.objects.all()
        if request.method=='POST':
            catname=request.POST['cat']
            brandname=request.POST['brand']
            
            c_obj=category(category=catname,brand_id=brandname) 
            c_obj.save()
            return redirect('cat')
        return render(request,'additem.html',{"bd":br})
    except Exception as e:
        print(e)
        return render(request,'categories.html')


def categories(request):
    cate=category.objects.select_related('brand')
    return render(request,'categories.html',{"cate":cate})  
def deletecate(request,id):
    category.objects.get(id=id).delete()
    return redirect('cat') 

def editcat(request,id):    
    cat=category.objects.get(id=id)
    br=brand.objects.all()
    return render(request,'editcategory.html',{"cate":cat,"brands":br})    

def updatecate(request,id):
    if request.method=='POST':
        catname=request.POST['cat']
        brandname=request.POST['brand']
        category.objects.filter(id=id).update(category=catname)
        brand.objects.filter(id=id).update(brand_name=brandname)
        return redirect('cat')    

def deal(request):
    return render(request,'dealoftheday.html')

def adddeal(request):
    return render(request,'adddeal.html')

def changecato(request):
    prooid = request.POST['brandid']
    data = category.objects.filter(brand_id=prooid)
    dataajson = [{'id':x.id,'category':x.category} for x in data]
    return JsonResponse({'dataitem':dataajson})


    return render(request,'addproduct.html')

def addProduct(request):
    #cate=category.objects.select_related('brand')
    cate=brand.objects.all()
    if request.method=='POST':
        cat=request.POST['cat']
        branditem=request.POST['brand']
        prod=request.POST['product']
        price=request.POST['price']
        # colr=request.POST['color']
        desc=request.POST['desc']
        # size=request.POST['size']
        discount=request.POST['discount']
        img=product(category_id=cat,brand_id=branditem,product_name=prod,price=price,description=desc,discount=discount)
        img.save()
    return render(request,'addproduct.html',{"cate":cate})

def changepro(request):
    proid = request.POST['brandid']
    data = category.objects.filter(brand_id=proid)
    datajson = [{'id':x.id,'category':x.category} for x in data]
    return JsonResponse({'dataitem':datajson})
def changeprod(request):
    prodata=request.POST['catid']
    pro=product.objects.filter(category_id=prodata)
    projson=[{'id':x.id,'product':x.product_name} for x in pro]
    return JsonResponse({'item':projson})

def addImage(request):
        cate=brand.objects.all()
        if request.method=='POST':
            product=request.POST['product']
            file=request.FILES['file']
            file_name=str(random())+file.name
            obj=FileSystemStorage()
            obj.save(file_name,file)

            imgobj=image(product_id=product,image=file_name)
            imgobj.save()
        return render(request,'addimage.html',{"cate":cate})
def viewProduct(request):
    prod=image.objects.all()
    brands=product.objects.all()
    return render(request,'viewproduct.html',{"product":prod,"brand":brands})

def editproduct(request,id):    
    pro=product.objects.filter(id=id)
    brands=brand.objects.all()
    return render(request,'editproduct.html',{"pro":pro,"brand":brands}) 
def updateprod(request,id):
    if request.method=='POST':
        catname=request.POST['cat']
        brandname=request.POST['brand']
        prod=request.POST['product']
        price=request.POST['price']
        desc=request.POST['desc']
        discount=request.POST['discount']
        product.objects.filter(id=id).update(brand_id=brandname,category_id=catname,product_name=prod,price=price,description=desc,discount=discount)
        return redirect('viewprod')         
