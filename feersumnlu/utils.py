import feersum_nlu

from feersumnlu.app_settings import FEERSUMNLU


def configure_feersum_nlu():
    feersum_nlu.configuration.api_key["AUTH_TOKEN"] = FEERSUMNLU["AUTH_TOKEN"]
    feersum_nlu.configuration.host = FEERSUMNLU["HOST"]
    return feersum_nlu


def match_feersum_nlu_faq(message):
    feersum_instance = configure_feersum_nlu()
    faq_api = feersum_nlu.FaqMatchersApi()
    response = faq_api.faq_matcher_retrieve(
        instance_name=FEERSUMNLU["MODEL"],
        text_input=feersum_instance.TextInput(text=message)
    )
    if response:
        return response[0].get("label", None)
    else:
        return "Sorry we were unable to match your question to an answer"
