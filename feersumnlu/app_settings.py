from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

FEERSUMNLU = {
    "AUTH_TOKEN": None,
    "HOST": None,
    "MODEL": None
}

for key, value in FEERSUMNLU.items():
    try:
        FEERSUMNLU[key] = settings.FEERSUMNLU[key]
    except AttributeError:
        raise ImproperlyConfigured("The %s setting must not be empty." % (key,))
