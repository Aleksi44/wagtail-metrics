from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks


class HomePage(Page):
    char_field = models.CharField(max_length=100, default=None, null=True)
    stream_field = StreamField([
        ('block', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False, default=None)),
            ('description', blocks.TextBlock(required=False, default=None)),
        ])),
        ('block_never_used', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False, default=None)),
        ])),
    ], default=None, blank=True)

    content_panels = [
        FieldPanel('char_field'),
        StreamFieldPanel('stream_field')
    ]
