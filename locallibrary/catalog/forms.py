from django import forms

class FormDueBack(forms.Form):
    new_date = forms.DateField(help_text="entre com a nova data para entrega (padrão 3 semanas)")
