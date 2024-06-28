from django.shortcuts import render
from django.http import HttpResponse
from account.decorators.requestsDecorator import page_in_construction
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.timezone import now
# Create your views here.
from .forms import userForm
from .models import User
@page_in_construction
def test(requests):
    return HttpResponse("<h1>ESTAS AQUI</h1>")

def logout_view(request):
    logout(request)
    return redirect('/')

@page_in_construction
def profile(requests):
    pass
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
                                        )
                user.save()
                return redirect("/home")
    return render(request,"registration/signup.html",context=
                  {
                      "DocumentName":"Registrarse",
                      "form":userForm(),
                      "styles":[
                          "account_login",
                          "account_signup"
                      ]
                  })