from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.timezone import now
from pages.utils import check_user,check_tasks,check_tags
# Create your views here.
def welcome(request):
    return render(request,"pages_home.html",context={
        "DocumentName":"Bienvenido",
        "styles":["pages_home"]}
        )
@login_required
def home(request): 
    return render(request,"pages_mainpage.html",context={
        "DocumentName":"Inicio",
        "user":check_user(request.user),
        "Task":check_tasks(request.user,request.GET.get('filter')),
        "Tags":check_tags(request.user),
        "styles":[
                    "pages_toggle",
                    "pages_mainpage",
                    
                ]
    })

