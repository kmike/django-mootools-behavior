from widget_tweaks.templatetags.widget_tweaks import set_data
from django.template import Library
register = Library()

@register.filter
def behave(field, names):
    ''' https://github.com/anutron/behavior support '''
    return set_data(field, 'behavior:'+names)
