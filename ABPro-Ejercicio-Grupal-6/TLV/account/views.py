from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.timezone import now
from .forms import userForm,AddressForm
from .models import User
from checkout.models import AnonymousOrder,Checkout
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/')
def signup(request):
    if request.method=="POST":
        form=userForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:
                user=User.objects.get(username=data["username"])
            except User.DoesNotExist:
                user=User.objects.create(first_name=data["first_name"],
                                            last_name=data["last_name"],
                                            username=data['username'],
                                            password=data["password"],
                                            email=data["email"],
                                            date_joined=now(),
                                            is_active=True,
                                            is_superuser=False,
                                            is_staff=False
                                        )
            
                user.save()
                return redirect("/account/login")
    return render(request,"registration/signup.html",context=
                  {
                      "DocumentName":"Registrarse",
                      "form":userForm(),
                      "styles":[
                          "account_login",
                          "account_signup"
                      ]
                  })
def profile(request):
    if request.user.is_staff:
        history=AnonymousOrder.objects.filter(seller=request.user).all()
    else:
        history=Checkout.objects.filter(client=request.user).all()
    return render(request,"profile.html",context=
                  {
                        "DocumentName":"Perfil",
                        "history":history,
                        "styles":[
                            "account_profile"
                        ]
                  })
def add_direction(request):
    return render(request,"add_direction.html",context=
                  {
                      "DocumentName":"Agregar Dirección",
                      "forms":{
                            "address":AddressForm()
                      },
                      "styles":[
                          "account_profile"
                      ]
                  })