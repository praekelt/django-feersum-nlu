from django.urls import reverse_lazy

from forms import FaqForm
from django.views.generic.edit import FormView

from utils import match_feersum_nlu_faq


class FaqFormView(FormView):
    template_name = "faqform.html"
    form_class = FaqForm
    success_url = reverse_lazy("faqquestion_thanks")

    def form_valid(self, form):
        self.request.session["answer"] = \
            match_feersum_nlu_faq(form.cleaned_data["text"])
        return super(FaqFormView, self).form_valid(form)
