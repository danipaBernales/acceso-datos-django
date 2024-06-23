from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from account.decorators.permissionsDecorator import staff_required,superuser_required
from .forms import *

from checkout.models import PayingMethod,Status,AnonymousOrder,AnonymousOrderDetail,Checkout,CheckoutDetail
from retail.models import *
import random 
import string
import json
from django.utils.timezone import now

# Create your views here.

@staff_required
def admin_view(request):
    try:
        if request.method=="POST":
            if request.POST["form_name"]=="producttype":
               
                form=ProductTypeForm(data=request.POST)
                if form.is_valid():
                    
                    data=form.cleaned_data
                    
                    try:

                        producttype=ProductType.objects.get(name=data["name"],category=data["category"])
                       
                    except ProductType.DoesNotExist:
                
                        producttype=ProductType.objects.create(name=data["name"],category=data["category"])
                        producttype.save()
                      
                raise Exception
            if request.POST["form_name"]=="category":   
                form=CategoryForm(data=request.POST)
                if form.is_valid():
                    data=form.cleaned_data
                    try:
                        category=Category.objects.get(name=data["name"])
                    except Category.DoesNotExist:
                        category=Category.objects.create(name=data["name"])
                        category.save()
                    raise Exception
            if request.POST["form_name"]=="product":
                data=request.POST
                brand=Brand.objects.get(id=data["brand"])
                producttype=ProductType.objects.get(id=data["productType"])
                product=Product.objects.create(
                    sku=random.randint(0,1_000_000_000),
                    name=data["name"],
                    spects=data["spects"],
                    price=data["price"],
                    brand=brand,
                    productType=producttype
                )
                product.save()
                for img in request.FILES.getlist("images"):
                    image=ProductImages(
                        title=img.name,
                        img=img,
                        product=product
                    )
                    image.save()
                
            if request.POST["form_name"]=="brand":
                form=BrandForm(data=request.POST)
                if form.is_valid():
                    data=form.cleaned_data
                    try:
                        brand=Brand.objects.get(name=data["name"])
                    except Brand.DoesNotExist:
                        brand=Brand.objects.create(name=data["name"])
                        brand.save()
                    raise Exception
        raise Exception
    except Exception as e:
        return render(request,template_name="admin_add_product.html",context={
            "DocumentName":"Administración",
            "form": ProductForm(),
            "images":ProductImageForm(),
            "category":CategoryForm(),
            "product":ProductTypeForm(),
            "brand":BrandForm(),
            "styles":["admin_add_product"],
            "garbage_code": "".join([random.choice(string.ascii_letters) for _ in range(0,16)])
        })

@staff_required
def take_order(request):
    if request.method=="POST":
        form=ProductTypeForm(data=request.POST)
        if form.is_valid():
            data=form.cleaned_data
    return render(request,"admin_anonymousorder.html",context=
                  {
                      "DocumentName":"Tomar Pedido",
                      "products":Product.objects.all(),
                      "forms":{
                    
                          "anonymousorder":AnonymousOrderForm()
                      },
                      "styles":[
                          "account_profile"
                      ],
                        "garbage_code": "".join([random.choice(string.ascii_letters) for _ in range(0,16)])
                      
                  })

@staff_required
def submit_order(request):
    if request.method=="POST":
        data = json.loads(request.body)
        anonymouseorder=AnonymousOrder(
            username=data["username"],
            paying_method=PayingMethod.objects.get(
                id=data["paying_method"]
                ),
            status=Status.objects.get(id=1),
            address=data["address"],
            seller=request.user
        )
        anonymouseorder.save()
        for product in data["purchase"]:
            chosenProduct=Product.objects.get(id=product["id"])
            print(chosenProduct)
            order=AnonymousOrderDetail.objects.create(
                product=chosenProduct,
                quantity=product["quantity"],
                anonymousorder=anonymouseorder
            )
            order.save()
        return JsonResponse({"purchase":True})
    return JsonResponse({"purchase":False})

@staff_required
def edit_order(request,ordertype,id):
    if ordertype=="Anonymous":
        order=AnonymousOrder.objects.get(id=id)
        orderDetail=AnonymousOrderDetail.objects.filter(anonymousorder=order)
    else:
        order=Checkout.objects.get(id=id)
        orderDetail=CheckoutDetail.objects.filter(checkout=order)
    return render(request,"admin_edit_order.html",context={
        "DocumentName":"Editar Pedido",
        "order":order,
        "orderdetail":orderDetail
    })