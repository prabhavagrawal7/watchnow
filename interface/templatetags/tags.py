from django import template
register = template.Library()

@register.filter
def dict_get(dictionary, value): 
    return dictionary.get(value)

