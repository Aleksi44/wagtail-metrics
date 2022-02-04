from django.utils.translation import gettext_lazy as _


class WagtailMetricsException(Exception):
    pass


class GoogleApiKeyNotSetException(WagtailMetricsException):
    def __init__(self):
        super().__init__(_("Google API key is not set"))
