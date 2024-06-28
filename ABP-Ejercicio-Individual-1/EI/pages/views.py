from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def welcome(request):
    return render(request,"pages_home.html",context={"DocumentName":"Bienvenido","styles":["pages_home"]})
@login_required
def home(request):
    return HttpResponse(f"<h1>Bienvendio, {request.user.username}</h1>")

def logout(request):
    logout(request)
    return redirect('/')