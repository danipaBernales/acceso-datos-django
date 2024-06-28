from django.shortcuts import render
from django.http import HttpResponse
from account.decorators.requestsDecorator import page_in_construction
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

@page_in_construction
def test(requests):
    return HttpResponse("<h1>ESTAS AQUI</h1>")

def logout_view(request):
    logout(request)
    return redirect('/')
