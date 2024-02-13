from django.db import models

from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from .custom_blocks import *

@register_snippet
class Header(models.Model):
    bg_image = models.ImageField(verbose_name='Задний фон в шапке', null=True, blank=True)
    name = models.CharField(max_length=150)
    speciality = models.CharField(max_length=150)
    slogan = models.CharField(max_length=150)

    panels = [
        FieldPanel('bg_image'),
        FieldPanel('name'),
        FieldPanel('speciality'),
        FieldPanel('slogan'),
    ]

    def __str__(self) -> str:
        return '"Шапка" сайта'

class FooterGalleryImage(Orderable):
    page = ParentalKey('Footer', on_delete=models.CASCADE, related_name='footer_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    url_image = models.URLField()

    panels = [
        FieldPanel('image'),
        FieldPanel('url_image'),
    ]

@register_snippet
class Footer(ClusterableModel):
    description = models.TextField(blank=True)

    panels = [
        FieldPanel('description'),
        InlinePanel('footer_images', label='Галерея футера'),
    ]
    
    def __str__(self) -> str:
        return 'Нижняя часть сайта'


# class FooterGalleryImage(Orderable):
#     page = ParentalKey(Footer, on_delete=models.CASCADE, related_name='footer_images')
#     image = models.ForeignKey(
#         'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
#     )

#     url_image = models.URLField()

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('url_image'),
#     ]