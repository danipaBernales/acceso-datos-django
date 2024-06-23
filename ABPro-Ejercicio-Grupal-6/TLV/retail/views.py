import random
import string
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from checkout.models import Shopping
from .models import Product,ProductImages
from account.models import Address
from checkout.models import PayingMethod
from django.utils.timezone import now
from datetime import timedelta

# Create your views here.
def home(request):
    try:
        cart_len=len(Shopping.objects.filter(client=request.user))
    except:
        cart_len=0
    
    product=Product.objects.all()
    
    return render(request,"retail_home.html",context={
        "DocumentName":"Te lo vendo",
        "products":product,
        "user": request.user.username if request.user.username!="AnonymousUser" else False,
        "garbage_code": "".join([random.choice(string.ascii_letters) for _ in range(0,16)]),
        "cart_len":cart_len,
        "styles":[
            "retail_home"
        ]
    })

@login_required
def shopping_cart(request):
    
    shopping=Shopping.objects.filter(client=request.user).all()
    total=sum([i.product.price*i.quantity for i in shopping])
    addresses=Address.objects.filter(client=request.user).all()
    paying_methods=PayingMethod.objects.all()
    return render(request,"retail_shopping_cart.html",context={
        "DocumentName":"Carro de compras",
        "garbage_code": "".join([random.choice(string.ascii_letters) for _ in range(0,16)]),
        "shopping_cart":shopping,
        "total":total,
        "addresses":addresses,
        "paying_method":paying_methods,
        "estimated_day": now()+timedelta(days=14)
    })