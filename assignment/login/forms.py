from django import forms

ROLES = ((0, 'Student'), (1, 'Tourist'), (2, 'Business'))

#the first two are test.
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class CreateAccount(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    Retype = forms.CharField(widget=forms.PasswordInput, max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    Type = forms.ChoiceField(choices = ROLES)
