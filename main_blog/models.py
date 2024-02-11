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


class CardBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    title = CharBlock(max_length=255)
    text = RichTextBlock()

    class Meta:
        template = 'main_blog/blocks/card_block.html'

class CardBlockList(StreamBlock):
    card = CardBlock()

class SecondBlock(StructBlock):
    image = ImageChooserBlock()
    title = RichTextBlock(max_length=255)
    text = RichTextBlock()

    class Meta:
        template = 'main_blog/blocks/second_section.html'

class SecondBlockImgRight(StructBlock):
    image = ImageChooserBlock()
    title = RichTextBlock(max_length=255)
    text = RichTextBlock()

    class Meta:
        template = 'main_blog/blocks/second_section_img_right.html'

class SecondBlockList(StreamBlock):
    section_left = SecondBlock()
    section_right = SecondBlockImgRight()


class AboutMeBlock(StructBlock):
    text = RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'main_blog/blocks/about_me.html'


class MainHomePage(Page):
    
    body = StreamField([
        ('textblock', RichTextBlock(required=False)),
        ('card_block_list', CardBlockList()),
        ('second_block_list', SecondBlockList()),
        ('about_me', AboutMeBlock()),
        ('gallery', ListBlock(ImageChooserBlock())),
        ('videos', ListBlock(EmbedBlock()))
    ], use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        return gallery_item.image if gallery_item else None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label='Gallery images'),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(max_length=250)
    
    panels = [
        FieldPanel('image'),
        FieldPanel('caption')
    ]
