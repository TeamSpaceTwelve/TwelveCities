from django import forms

SCORES = ((1, '1'), (2, '2'), (3, '3'),(4, '4'), (5, '5'))

class search(forms.Form):
    search = forms.CharField(label='Search Items', max_length=100)

class review(forms.Form):
    review = forms.CharField(widget=forms.Textarea)
    score = forms.ChoiceField(choices = SCORES)