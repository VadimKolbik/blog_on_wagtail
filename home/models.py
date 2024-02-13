from django.db import models


# Create your models here.
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.blocks import StructBlock, CharBlock, RichTextBlock, StreamBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from .custom_blocks import *

class HomePage(Page):
    body = StreamField([
        ('textblock', RichTextBlock(required=False)),
        ('card_block_list', CardBlockList()),
        ('second_block_list', SecondBlockList()),
        ('about_me', AboutMeBlock()),
        ('gallery', ListBlock(ImageChooserBlock())),
        ('videos', ListBlock(EmbedBlock()))
    ], use_json_field=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]