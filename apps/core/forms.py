from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')
