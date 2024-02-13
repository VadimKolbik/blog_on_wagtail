from django import template
from home.snippets import Header, Footer
from home.models import HomePage

register = template.Library()

@register.inclusion_tag('home/tags/header.html', takes_context=True)
def header_tag(context):
    return {
        'header': Header.objects.first(),
        'request': context['request'],
        'main_menu': HomePage.objects.first().get_children().live()
    }

@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'footer': Footer.objects.first(),
        'request': context['request'],
    }