from django.contrib import admin
from .models import Tag,Color,Task,Status

# Register your models here.
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Status)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter=["owner"]