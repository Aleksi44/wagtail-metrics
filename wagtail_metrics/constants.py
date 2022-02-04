from django.conf import settings

WAGTAIL_METRICS_DEFAULT_EXCLUDE = getattr(settings, 'WAGTAIL_METRICS_DEFAULT_EXCLUDE', [
    'sites_rooted_here',
    'aliases',
    'revisions',
    'group_permissions',
    'view_restrictions',
    'workflow_states',
    'wagtail_admin_comments',
    'subscribers',
    'id',
    'path',
    'depth',
    'numchild',
    'translation_key',
    'draft_title',
    'has_unpublished_changes',
    'url_path',
    'go_live_at',
    'expire_at',
    'expired',
    'locked',
    'locked_at',
    'locked_by',
    'latest_revision_created_at',
    'live_revision',
    'alias_of',
    'page_ptr',
    'index_entries',
    'content_type'
])

WAGTAIL_METRICS_INDENT_JSON = getattr(settings, 'WAGTAIL_METRICS_INDENT_JSON', None)
WAGTAIL_METRICS_GOOGLE_API_KEY = getattr(settings, 'WAGTAIL_METRICS_GOOGLE_API_KEY', None)
WAGTAIL_METRICS_SEPARATOR = getattr(settings, 'WAGTAIL_METRICS_SEPARATOR', '__')
