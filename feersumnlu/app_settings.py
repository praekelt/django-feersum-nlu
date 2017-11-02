from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

FEERSUMNLU = {
    "AUTH_TOKEN": None,
    "HOST": None
}

for key, value in FEERSUMNLU.items():
    try:
        FEERSUMNLU[key] = settings.FEERSUMNLU[key]
    except AttributeError:
        raise ImproperlyConfigured("The ", key, " setting must not be empty.")
