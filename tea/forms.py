from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
