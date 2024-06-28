from django import template
from django.utils.timezone import now
register=template.Library()

@register.filter
def is_expired(date):
    return now().date()>date

@register.filter
def is_complete(status):
    return status=="Completado"