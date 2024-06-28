from django import forms
from django.utils.timezone import now
from .models import Task,Status,Tag
from account.models import User
#AutoForm
class TaskModelForm(forms.ModelForm):   
    class Meta:
        model=Task
        fields="__all__"

class TaskForm(forms.Form):
    title=forms.CharField(max_length=100,label="Titulo")
    description=forms.CharField(max_length=1000,label="Descripcion", required=False)
    expire_date=forms.DateField(label="Fecha limite",widget=forms.DateInput(attrs={'type': 'date'}),initial=now().today())
    status=forms.ChoiceField()
    tag=forms.ChoiceField()
    def __init__(self,user:str="",*args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        user=User.objects.get(username=user)
        self.fields["status"].choices=[(obj.id,obj.name) for obj in Status.objects.all()]
        #This should be Tag.objects.filter(owner=user)
        self.fields["tag"].choices=[(obj.id,obj.name) for obj in Tag.objects.all()]