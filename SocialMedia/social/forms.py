from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    query = forms.CharField(
        required=True,
        widget=forms.Textarea
    )