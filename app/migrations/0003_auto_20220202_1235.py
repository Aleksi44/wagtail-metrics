# Generated by Django 3.2.12 on 2022-02-02 12:35

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='char_field',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='stream_field',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock())], blank=True, default=None),
        ),
    ]
