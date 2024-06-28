from tasks.models import Task,Tag
from django.contrib.auth import get_user_model
def check_user(user):
    return user.username if str(user)!="AnonymousUser" else False
def check_tasks(user,filter):
    if not check_user(user):
        return False
    else:
        user_object=get_user_model().objects.get(username=user.username)
        try:
            if filter!=None:
                tag=Tag.objects.get(name=filter,owner=user_object)
                task=Task.objects.filter(owner=user_object,tag=tag).order_by("-expire_date")
            else:
                task=Task.objects.filter(owner=user_object).order_by("-expire_date")
            return task
        except Task.DoesNotExist:
            return False
def check_tags(user):
    if not check_user(user):
        return False
    else:
        user_object=get_user_model().objects.get(username=user.username)
        try:
            tag=Tag.objects.filter(owner=user_object)
            return tag
        except Task.DoesNotExist:
            return False