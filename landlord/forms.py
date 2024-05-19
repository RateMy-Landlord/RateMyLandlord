from django import forms
from.models import Landlord

class LandlordForm(forms.ModelForm):
    class Meta:
        model = Landlord
        fields = ['name', 'address']