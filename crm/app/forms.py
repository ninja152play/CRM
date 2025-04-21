from django import forms
from django.db.models import Q

from .models import Campaign, Service, Contract, Lead, ActiveClient

class CampaignForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # или SelectMultiple для списка
        required=True
    )

    class Meta:
        model = Campaign
        fields = ['name', 'services', 'channel', 'budget']


    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance


services = forms.ModelMultipleChoiceField(
    queryset=Service.objects.all(),
    widget=forms.CheckboxSelectMultiple(),
    required=True
)


class ActiveClientForm(forms.ModelForm):
    class Meta:
        model = ActiveClient
        fields = ['name', 'lead', 'contract', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lead'].queryset = Lead.objects.filter(status='ACTIVE')