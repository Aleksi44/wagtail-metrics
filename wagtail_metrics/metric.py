from django.utils.text import slugify
from wagtail_metrics import constants

LIMIT_VALUE = 50


class Metric:
    def __init__(self, key):
        self.key = key
        self.counter = 0
        self.values = {}

    def __lt__(self, metric):
        return self.counter > metric.counter

    def __dict__(self):
        return {
            'counter': self.counter,
            'values': self.values
        }

    def add_value(self, value, page_url=None):
        self.counter += 1
        if not isinstance(value, str):
            value = slugify(value)
        if self.key not in constants.WAGTAIL_METRICS_VALUE_LIMIT_EXCLUDE:
            if len(value) > constants.WAGTAIL_METRICS_VALUE_LIMIT:
                value = value[:constants.WAGTAIL_METRICS_VALUE_LIMIT] + '...'
        if value in self.values:
            self.values[value]['counter'] += 1
        else:
            self.values[value] = {
                'counter': 1,
                'pages': []
            }
        if page_url:
            self.values[value]['pages'].append(page_url)
