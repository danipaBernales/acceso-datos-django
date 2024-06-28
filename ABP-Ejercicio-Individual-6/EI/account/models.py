from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# Create your models here.

class User(AbstractUser):
    pass
class recovery_key(models.Model):
    key=models.IntegerField()
    expire_date=models.DateTimeField(null=False,blank=False,default=now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
