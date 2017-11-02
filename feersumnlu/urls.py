from django.conf.urls import url
from django.views.generic import TemplateView

from .views import FaqFormView

urlpatterns = [
    url(r'^$', FaqFormView.as_view(), name='faqquestion_index'),
    url(r'^thanks/$', TemplateView.as_view(template_name="faqform_thanks.html"), name='faqquestion_thanks')
]