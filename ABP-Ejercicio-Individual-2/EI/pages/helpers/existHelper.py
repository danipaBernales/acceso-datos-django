from tasks.models import Task
from django.contrib.auth import get_user_model
def check_user(user):
    return user.username if str(user)!="AnonymousUser" else False
def check_tasks(user):
    if not check_user(user):
        return False
    else:
        user_object=get_user_model().objects.get(username=user.username)
        try:
            task=Task.objects.filter(owner=user_object)
            return task
        except Task.DoesNotExist:
            return False