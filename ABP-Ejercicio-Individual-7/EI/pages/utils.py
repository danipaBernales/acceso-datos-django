from tasks.models import Task,Tag,Status
from django.contrib.auth import get_user_model

def check_user(user):
    return user.username if str(user)!="AnonymousUser" else False
def check_tasks(user,tag,status,completed=False):
    if not check_user(user):
        return False
    else:
        user_object=get_user_model().objects.get(username=user.username)
        try:
            query_filter={"owner":user_object}
            if tag!=None:
                query_filter["tag"]=Tag.objects.get(name=tag,owner=user_object)
            if status!=None:
                query_filter["status"]=Status.objects.get(name=status)
            if completed:
                query_filter["status"]=Status.objects.get(name="Completado")
            else:
                task=Task.objects.filter(**query_filter).order_by("-expire_date").exclude(status=Status.objects.get(name="Completado"))
                return task
            task=Task.objects.filter(**query_filter).order_by("-expire_date")
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