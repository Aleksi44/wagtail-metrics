from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks


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
    ], default=None, blank=True, use_json_field=True)

    content_panels = [
        FieldPanel('char_field'),
        FieldPanel('stream_field')
    ]
