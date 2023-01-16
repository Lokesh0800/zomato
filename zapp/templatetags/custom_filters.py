from django import template

register = template.Library()

@register.filter
def make_dict(val):
    return eval(val)