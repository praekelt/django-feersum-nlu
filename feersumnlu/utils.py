import feersum_nlu

from feersumnlu.app_settings import FEERSUMNLU


def configure_feersum_nlu():
    feersum_nlu.configuration.api_key["AUTH_TOKEN"] = FEERSUMNLU["AUTH_TOKEN"]
    feersum_nlu.configuration.host = FEERSUMNLU["HOST"]
    return feersum_nlu
