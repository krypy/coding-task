from django.forms import ModelForm
from crud.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'iban']