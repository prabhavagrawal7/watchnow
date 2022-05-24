from django import template
register = template.Library()


@register.filter
def dict_get(dictionary, value):
    return dictionary.get(value)


@register.filter
def div(value, arg):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int(value)
        arg = int(arg)
        if arg:
            return round(value / arg, 1)
    except:
        pass
    return ''
