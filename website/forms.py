from django import forms
from django.core.validators import RegexValidator


class mastermaind_reg_form(forms.Form):
    fio = forms.CharField(max_length=250)
    phoneNumber = forms.RegexField(regex=r"^\+?1?\d{8,15}$", max_length=16)
    email = forms.EmailField(max_length=150)
    request = forms.CharField(widget=forms.Textarea)
