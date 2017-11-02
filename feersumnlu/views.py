from forms import FaqForm
from django.views.generic.edit import FormView


class FaqFormView(FormView):
    template_name = "faqform.html"
    form_class = FaqForm
    success_url = "/thanks/"

    def form_valid(self, form):
        print form
        return super(FaqFormView, self).form_valid(form)
