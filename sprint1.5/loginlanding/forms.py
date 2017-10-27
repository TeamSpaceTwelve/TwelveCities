from django import forms

class search(forms.Form):
    search = forms.CharField(label='Search Items', max_length=100)
