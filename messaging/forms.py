from django import forms
from messaging.models import MessageGroup
from messaging.models import MessageContent


class CreateMessageForm(forms.Form):
    class Meta:
        model = MessageContent, MessageGroup

    recipient = forms.CharField(
            label='Recipient',
            widget=forms.TextInput(attrs={
                'placeholder': "e.g. doctor strange, wanda, etc.",
                'required': True,
                'size': 50,
                'class': 'w-full rounded border px-4 py-2'
            })
        )
    title = forms.CharField(
            label='Subject',
            widget=forms.TextInput(attrs={
                'placeholder': "e.g. I'm dying, help im pregnant, etc.",
                'required': True,
                'size': 50,
                'class': 'w-full rounded border px-4 py-2'
            })
        )
    priority = forms.ChoiceField(
            label='Priority',
            widget=forms.RadioSelect(attrs={
                'required': True
            }),
            choices=[('0', 'Low'), ('1', 'Medium'), ('2', 'High')]
        )
    content = forms.CharField(
            label='Content',
            widget=forms.Textarea(attrs={
                'placeholder': "e.g. those drugs you gave me are hitting hard fam..",
                'max_length': 100,
                'required': True,
                'rows': 3,
                'cols': 50,
                'class': 'w-full px-4 py-2 rounded border align-middle'
            })
        )
