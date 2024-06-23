from django.shortcuts import render
def blocked(func):
    def wrapper(requests):
        return render(requests,"403.html",status=403)
    return wrapper

def page_in_construction(func):
    def wrapper(request):
        return render(request,"status_pages/503.html")
    return wrapper