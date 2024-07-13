from django import forms

class EmailForm(forms.Form):
    email_address = forms.EmailField(label='Email Address')
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
