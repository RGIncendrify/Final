from django import template

register = template.Library()

@register.filter
def getattribute(value, arg):
    """Retrieves an attribute of an object dynamically."""
    return getattr(value, arg, '')