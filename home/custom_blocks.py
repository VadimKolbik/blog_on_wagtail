from wagtail.blocks import StructBlock, CharBlock, RichTextBlock, StreamBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock

class CardBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    title = CharBlock(max_length=255)
    text = RichTextBlock()

    class Meta:
        template = 'home/blocks/card_block.html'

class CardBlockList(StreamBlock):
    card = CardBlock()

class SecondBlock(StructBlock):
    image = ImageChooserBlock()
    title = RichTextBlock(max_length=255)
    text = RichTextBlock()

    class Meta:
        template = 'home/blocks/second_section.html'

class SecondBlockImgRight(StructBlock):
    image = ImageChooserBlock()
    title = RichTextBlock(max_length=255)
    text = RichTextBlock()

    class Meta:
        template = 'home/blocks/second_section_img_right.html'

class SecondBlockList(StreamBlock):
    section_left = SecondBlock()
    section_right = SecondBlockImgRight()


class AboutMeBlock(StructBlock):
    text = RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'home/blocks/about_me.html'

class AboutMeBlockImgLeft(StructBlock):
    text = RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'home/blocks/about_me.html'


class AboutMeBlockList(StreamBlock):
    section_right = AboutMeBlock()
    section_left = AboutMeBlockImgLeft()
