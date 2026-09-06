from django import forms
from django.contrib.auth import get_user_model

from .models import TicketModel

User = get_user_model()

class TicketCreateForm(forms.ModelForm):
    '''Creates a new request'''
    class Meta:
        model = TicketModel
        fields = ['description']
        widgets = {'description': forms.Textarea()}


class TransferForm(forms.Form):
    '''Transfer the request to another user'''
    new_user = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='tech'),#FIXME - group tech
        label='Новый исполнитель',
        empty_label='Выберите исполнителя'
    )