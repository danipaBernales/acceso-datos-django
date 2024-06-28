from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.timezone import now
from pages.utils import check_user,check_tasks,check_tags
from tasks.models import Status
# Create your views here.
def welcome(request):
    return render(request,"pages_home.html",context={
        "DocumentName":"Bienvenido",
        "styles":["pages_home"]}
        )
@login_required
def home(request): 
    tag=request.GET.get('tag') if request.GET.get('tag')!="-------" else None
    status=request.GET.get('state') if request.GET.get('state')!="-------" else None
    task=check_tasks(request.user,tag,status)
    complete_task=check_tasks(request.user,tag,status,True)
    return render(request,"pages_mainpage.html",context={
        "DocumentName":"Inicio",
        "user":check_user(request.user),
        "Task":task,
        "completed_task":complete_task,
        "Tags":check_tags(request.user),
        "Statuses":Status.objects.all(),
        "styles":[
                    "pages_toggle",
                    "pages_mainpage",
                    
                ]
    })

