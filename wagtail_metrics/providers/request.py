import logging
import requests
from wagtail_metrics import constants

logger = logging.getLogger(__name__)


def run(checkup, page):
    try:
        response = requests.get(page.get_full_url())
        checkup.add_metric(
            'request%sstatus_code' % constants.WAGTAIL_METRICS_SEPARATOR,
            response.status_code,
            page.get_full_url()
        )
    except requests.exceptions.RequestException as err:
        logger.error(str(err))
