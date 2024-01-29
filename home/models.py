from django.db import models

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

@register_snippet
class Header(models.Model):
    bg_image = models.ImageField(verbose_name='Задний фон в шапке', null=False, blank=False)
    name = models.CharField(max_length=150)
    speciality = models.CharField(max_length=150)
    slogan = models.CharField(max_length=150)

    def __str__(self) -> str:
        return '"Шапка" сайта'

@register_snippet
class Footer(models.Model):
    
    def __str__(self) -> str:
        return 'Нижняя часть сайта'


# class FooterGalleryImage(Orderable):
#     pass