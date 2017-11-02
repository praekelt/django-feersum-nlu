from django import forms
from django.utils.translation import ugettext_lazy as _


class FaqForm(forms.Form):
    text = forms.CharField(
        max_length=255,
        label=_("Text"),
        widget=forms.TextInput(
            attrs={
                "placeholder": _("User says..."),
                "class": "Field-textInput"
            }
        )
    )
