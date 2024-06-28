from django.db import models
from account.models import User
from django.core.validators import MaxValueValidator
import datetime
class Status(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.

class Color(models.Model):
    R=models.IntegerField(validators=[MaxValueValidator(255)])
    G=models.IntegerField(validators=[MaxValueValidator(255)])
    B=models.IntegerField(validators=[MaxValueValidator(255)])
    def to_hex(self):
        return '#{:02x}{:02x}{:02x}'.format(self.R,self.G,self.B)
    def __str__(self):
        return self.to_hex()
    class Meta:
        unique_together=('R','G','B')
class Tag(models.Model):
    name=models.CharField(max_length=100)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} own by {self.owner}"
class Task(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(default="No description has been provided")
    expire_date=models.DateField(blank=False,null=False,default=datetime.date.today())
    status=models.ForeignKey(Status,on_delete=models.SET_NULL,null=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f"{self.title}"