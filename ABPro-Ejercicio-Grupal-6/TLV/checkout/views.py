from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Shopping,Checkout,CheckoutDetail,PayingMethod,Status
from retail.models import Product
from django.http import JsonResponse
from account.models import Address

from django.utils.timezone import now
from datetime import timedelta

import json
# Create your views here.
@login_required
def paying_page(request):
    addresses=Address.objects.filter(client=request.user).all()
    paying_methods=PayingMethod.objects.all()
    return render(request,"checkout_paying.html",context={
        "DocumentName":"Proceso",
        "addresses":addresses,
        "paying_method":paying_methods,
        "estimated_day": now()+timedelta(days=14)
    })
@login_required
def buy(request):
    if request.method=="POST":
        data = json.loads(request.body)
        product=Product.objects.get(id=data["product_id"])
        shopping=Shopping.objects.create(product=product,quantity=data["quantity"],client=request.user)
        shopping.save()
        lenght=len(Shopping.objects.filter(client=request.user))
        return JsonResponse({"response":True,"len":lenght})
    return JsonResponse({"response":False})

@login_required
def remove(request,id):
    product=Product.objects.get(id=id)
    Shopping.objects.get(product=product,client=request.user)
    return JsonResponse({"response":"Se elimino el producto del carrito"})

@login_required
def process(request):
    if request.method=="POST":
        data = json.loads(request.body)
        products=Shopping.objects.filter(client=request.user).all()
        checkout=Checkout.objects.create(
            client=request.user,
            paying_method=PayingMethod.objects.get(id=data["paying_method"]),
            status=Status.objects.get(id=1),
            address=Address.objects.get(client=request.user,id=data["address"])
        )
        checkout.save()
        for product in products:
            checkout_detail=CheckoutDetail.objects.create(
                product=product.product,
                quantity=product.quantity,
                checkout=checkout
            )
            product.delete()
            checkout_detail.save()
        return JsonResponse({"response":True})
    return  JsonResponse({"response":False})

@login_required
def order_detail(request,id):
    ticket=Checkout.objects.get(id=id,client=request.user)
    return render(request,"checkout_detail.html",context={
        "DocumentName":"Detalle de boleta",
        "ticket":ticket,
        "ticket_details":CheckoutDetail.objects.filter(
                checkout=ticket).all()
    })
