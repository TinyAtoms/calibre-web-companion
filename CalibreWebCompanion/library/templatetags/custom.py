from django import template
from ..models import Books

register = template.Library
print("I ACTUALLY CAME HEReEe")

@register.simple_tag
def dummy(): 
    return Books.objects.count()