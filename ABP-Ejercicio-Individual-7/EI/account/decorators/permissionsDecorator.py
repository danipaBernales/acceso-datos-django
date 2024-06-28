from django.shortcuts import render

#this is not finished yet
def permission_required(func,exclusive=True):
    def wrapper(request):
        return func(request)
    return wrapper

def superuser_required(func):
    def wrapper(request):
        if request.user.is_superuser:
            func(request)
        return render(request,"403.html",status=403)
    return wrapper


def debug(status):
    if status:
        def decorator(func):
            return func
    else:
        def decorator(func):
            def wrapper(request,uri_query):
                try:
                    return func(request,uri_query)
                except:
                    return render(request,"403.html",status=403)
            return wrapper
    return decorator