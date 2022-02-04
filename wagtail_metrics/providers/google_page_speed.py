import logging
import requests
import time
from wagtail_metrics import constants
from wagtail_metrics.exceptions import GoogleApiKeyNotSetException

logger = logging.getLogger(__name__)


def percentage(value):
    if value:
        return str(round(value * 100))
    return ''


def run(checkup, page):
    if not constants.WAGTAIL_METRICS_GOOGLE_API_KEY:
        raise GoogleApiKeyNotSetException
    time.sleep(1)
    response = requests.get(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
        "?url=%s&%s&fields=lighthouseResult/categories/*/score&prettyPrint=false"
        "&strategy=mobile&category=performance&category=best-practices"
        "&category=accessibility&category=seo"
        % (page.get_full_url(), constants.WAGTAIL_METRICS_GOOGLE_API_KEY))
    if response.status_code == 200 and 'application/json' in response.headers['Content-Type']:
        pagespeed_json = response.json()
        checkup.add_metric(
            'google_page_speed%sperformance' % constants.WAGTAIL_METRICS_SEPARATOR,
            percentage(pagespeed_json['lighthouseResult']['categories']['performance']['score']),
            page.get_full_url()
        )
        checkup.add_metric(
            'google_page_speed%saccessibility' % constants.WAGTAIL_METRICS_SEPARATOR,
            percentage(pagespeed_json['lighthouseResult']['categories']['accessibility']['score']),
            page.get_full_url()
        )
        checkup.add_metric(
            'google_page_speed%sbest_practices' % constants.WAGTAIL_METRICS_SEPARATOR,
            percentage(pagespeed_json['lighthouseResult']['categories']['best-practices']['score']),
            page.get_full_url()
        )
        checkup.add_metric(
            'google_page%sspeed_seo' % constants.WAGTAIL_METRICS_SEPARATOR,
            percentage(pagespeed_json['lighthouseResult']['categories']['seo']['score']),
            page.get_full_url()
        )
    else:
        logger.error(str(response.json()['error']['message']))
