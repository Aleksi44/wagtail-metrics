import json
import logging
from django.conf import settings
from wagtail.core.models import Page, Site
from wagtail_metrics.metric import Metric
from wagtail_metrics import constants
from wagtail_metrics.exceptions import WagtailMetricsException

logger = logging.getLogger(__name__)
DEFAULT_PROVIDERS = ['wagtail_page']


class Checkup:
    def __init__(self, providers=None):
        self.metrics = []
        self.i18n_enable = getattr(settings, 'WAGTAIL_I18N_ENABLED', False)
        self.providers = providers if providers else DEFAULT_PROVIDERS

    def __dict__(self):
        result = {}
        self.metrics.sort()
        for metric in self.metrics:
            result[metric.key] = metric.__dict__()
        return result

    @staticmethod
    def _get_provider_module(provider_name):
        return __import__('wagtail_metrics.providers.%s' % provider_name, fromlist=['function'])

    def add_page(self, page):
        if not isinstance(page, Page):
            return
        for provider_name in self.providers:
            provider_module = self._get_provider_module(provider_name)
            provider_function = getattr(provider_module, 'run')
            try:
                provider_function(self, page)
            except WagtailMetricsException as err:
                logger.error(str(err))

    def add_site(self, site):
        if not isinstance(site, Site):
            return
        for page in site.root_page.get_descendants(inclusive=True).specific():
            self.add_page(page)
            if self.i18n_enable:
                for page_alternate in page.get_translations().exclude(alias_of__isnull=False):
                    self.add_page(page_alternate)

    def add_metric(self, key, value, page_url=None, initialize=False):
        if key not in constants.WAGTAIL_METRICS_DEFAULT_EXCLUDE:
            metric, created = self._get_or_create_metric(key)
            if not initialize:
                metric.add_value(value, page_url=page_url)
            if created:
                self.metrics.append(metric)

    def to_json(self):
        return json.dumps(self.__dict__(), indent=constants.WAGTAIL_METRICS_INDENT_JSON)

    def _get_or_create_metric(self, key):
        for metric in self.metrics:
            if metric.key == key:
                return metric, False
        return Metric(key=key), True
