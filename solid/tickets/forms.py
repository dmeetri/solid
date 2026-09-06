from django import forms

from .models import TicketModel

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = ['description']
        widgets = {'description': forms.Textarea()}
