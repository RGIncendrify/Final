from django import forms
from .models import Beneficiation

class BeneficiationForm(forms.ModelForm):
    class Meta:
        model = Beneficiation
        fields = '__all__'  # Include all fields from the Beneficiation model
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }