from django import template

register = template.Library()

@register.filter(name='my_cut')
def my_cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

# register.filter('my_cut', my_cut)

@register.filter(name='compare_numbers')
def compare_numbers(value, arg):
    if value > arg:
        return str(value)+" is larger than "+str(arg)
    elif value == arg:
        return "They are the same"
    else:
        return str(value)+" is smaller than "+str(arg)

# register.filter('compare_numbers', compare_numbers)