from django import template

from ..models import FamilyInvite, CompanyInvite

register = template.Library()


# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/
@register.inclusion_tag('groups/_badge.html', takes_context=True)
def invites_badge(context, invite_type):
    if invite_type == 'family':
        return {
            'invite_count': context['user'].familyinvite_received.filter(
                status=0).count()
        }
    else:
        return {
            'invite_count': context['user'].companyinvite_received.filter(
                status=0).count()
        }


@register.inclusion_tag('groups/_dot.html', takes_context=True)
def invites_dot(context, invite_type):
    if invite_type == 'family':
        return {
            'invites': bool(context['user'].familyinvite_received.filter(status=0))}
    else:
        return {
            'invites': bool(context['user'].companyinvite_received.filter(status=0))}
