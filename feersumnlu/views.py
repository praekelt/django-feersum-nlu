from django.urls import reverse_lazy
from feersum_nlu import FaqMatchersApi

from forms import FaqForm
from django.views.generic.edit import FormView

from feersumnlu import utils
from feersumnlu.app_settings import FEERSUMNLU


class FaqFormView(FormView):
    template_name = "faqform.html"
    form_class = FaqForm
    success_url = reverse_lazy("feersumnlu:faqquestion_thanks")

    def form_valid(self, form):
        feersum_nlu = utils.configure_feersum_nlu()
        faq_api = FaqMatchersApi()
        response = faq_api.faq_matcher_retrieve(
            instance_name=FEERSUMNLU["MODEL"],
            text_input=feersum_nlu.TextInput(text=form.cleaned_data["text"])
        )
        if response:
            self.request.session["answer"] = response[0].get("label", None)
        else:
            self.request.session["answer"] = "Sorry we were unable to match " \
                                             "your question to an answer"
        return super(FaqFormView, self).form_valid(form)
