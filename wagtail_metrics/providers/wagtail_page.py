from wagtail.core.fields import StreamValue, StreamBlock, StreamField
from wagtail.core.blocks import StructValue, StructBlock
from wagtail_metrics import constants


def _inspect_field(checkup, block, key='', initialize=False, page=None):
    if isinstance(block, StreamValue):
        for stream in block:
            _inspect_field(
                checkup,
                stream.value,
                key=key + constants.WAGTAIL_METRICS_SEPARATOR + stream.block.name,
                initialize=initialize,
                page=page
            )
    elif isinstance(block, StreamBlock):
        for block_key, block_child in block.child_blocks.items():
            _inspect_field(
                checkup,
                block_child,
                key=key + constants.WAGTAIL_METRICS_SEPARATOR + block_key,
                initialize=initialize,
                page=page
            )
    elif isinstance(block, StructValue):
        for block_key, _ in block.block.child_blocks.items():
            block_value = block[block_key]
            _inspect_field(
                checkup,
                block_value,
                key=key + constants.WAGTAIL_METRICS_SEPARATOR + block_key,
                initialize=initialize,
                page=page
            )
    elif isinstance(block, StructBlock):
        for block_key, block_child in block.child_blocks.items():
            _inspect_field(
                checkup,
                block_child,
                key=key + constants.WAGTAIL_METRICS_SEPARATOR + block_key,
                initialize=initialize,
                page=page
            )
    elif isinstance(block, list):
        for block_child in block:
            if block_child:
                if hasattr(block_child, 'block'):
                    _inspect_field(
                        checkup,
                        block_child,
                        key=key + constants.WAGTAIL_METRICS_SEPARATOR + block_child.block.name,
                        initialize=initialize,
                        page=page
                    )
                else:
                    _inspect_field(
                        checkup,
                        block_child,
                        key=key,
                        initialize=initialize,
                        page=page
                    )
    else:
        return checkup.add_metric(
            key,
            block,
            page.get_full_url() if page else None,
            initialize=initialize
        )
    return


def run(checkup, page):
    for attribute in page._meta.get_fields():
        if isinstance(attribute, StreamField):
            _inspect_field(
                checkup,
                attribute.stream_block,
                initialize=True,
                key=(
                    constants.WAGTAIL_METRICS_STREAM_FIELD_KEY if
                    constants.WAGTAIL_METRICS_STREAM_FIELD_KEY else attribute.name
                )
            )
    for attribute in page._meta.get_fields():
        try:
            block = getattr(page, attribute.name)
            if isinstance(block, StreamValue):
                key = constants.WAGTAIL_METRICS_STREAM_FIELD_KEY if \
                    constants.WAGTAIL_METRICS_STREAM_FIELD_KEY else attribute.name
            else:
                key = attribute.name
            _inspect_field(
                checkup,
                block,
                key=key,
                page=page
            )
        except AttributeError:
            pass
