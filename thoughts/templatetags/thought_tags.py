from django import template

# thoughts.forms
from ..forms import ThoughtForm

register = template.Library()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/
@register.inclusion_tag('thoughts/_form.html')
def thought_form():
    form = ThoughtForm()
    return {'form': form }
