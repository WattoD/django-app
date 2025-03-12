from django import template
from members.models import CustomUser
import datetime

register = template.Library()

@register.simple_tag()
def date():
    return datetime.date.today()

@register.simple_tag()
def trim(text, length=10, suffix='...'):
    if len(text) > length:
        return f"{text[:length]}{suffix}"
    return text

@register.inclusion_tag('partials/user_list.html')
def users():
    custom_users = CustomUser.objects.all()
    return {'users': custom_users}