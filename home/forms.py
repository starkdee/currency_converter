from django import forms


class CurrencyForm(forms.Form):
    amount = forms.FloatField(label='', widget=forms.NumberInput(attrs={'class': 'form-input', 'id': 'amount', 'placeholder': 'Amount'}))
    c_from = forms.CharField(label='', max_length=3, widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'cur-from'}))
    c_to = forms.CharField(label='', max_length=3, widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'cur-to'}))