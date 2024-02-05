from django import template
from home.models import Header, Footer

register = template.Library()

@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header_tag(context):
    return {
        'header': Header.objects.first(),
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'footer': Footer.objects.first(),
        'request': context['request'],
    }