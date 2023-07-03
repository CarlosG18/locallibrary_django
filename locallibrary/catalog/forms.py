from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class FormDueBack(forms.Form):
    new_date = forms.DateField(help_text="entre com a nova data para entrega (padrão 3 semanas)")

    def clean_new_date(self):
        data = self.cleaned_data['new_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data < datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data