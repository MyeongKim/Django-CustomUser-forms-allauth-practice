from django import forms
from django.forms import ModelForm

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'my-class', 'title': 'Your name'}))
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
