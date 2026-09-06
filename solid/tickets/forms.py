from django import forms
from django.conf import settings

from .models import TicketModel

class TicketCreateForm(forms.ModelForm):
    '''Creates a new request'''
    class Meta:
        model = TicketModel
        fields = ['description']
        widgets = {'description': forms.Textarea()}


class TransferForm(forms.Form):
    '''Transfer the request to another user'''
    new_user = forms.ModelChoiceField(
        queryset=settings.AUTH_USER_MODEL.objects.filter(groups__name='tech'),#FIXME - group tech
        label='Новый исполнитель',
        empty_label='Выберите исполнителя'
    )