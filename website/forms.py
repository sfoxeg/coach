from django import forms
from .models import Mastermind_reg


class Mastermind_reg_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
    class Meta:
        model = Mastermind_reg
        fields = ['fio', 'phone', 'email', 'request']
        label = ''
        widgets = {
            'fio': forms.TextInput(attrs={'placeholder': 'ФИО'}),
            'phone': forms.TextInput(attrs={'placeholder': '7XXXXXXXXXX'}),
            'email': forms.TextInput(attrs={'placeholder': 'chemodan@bolshoy.ru'}),
            'request': forms.Textarea(attrs={'placeholder': 'Какой у вас запрос'})
        }
