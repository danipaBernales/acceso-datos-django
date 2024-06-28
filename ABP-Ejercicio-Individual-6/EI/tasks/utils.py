from tasks.models import Comments
def check_comments(task):
    try:
        return Comments.objects.filter(task=task)
    except Comments.DoesNotExist:
        return False