from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['value']

class TemporaryMessageForm(forms.Form):
    value = forms.CharField(max_length=255, required=True)