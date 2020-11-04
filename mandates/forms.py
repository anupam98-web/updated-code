from django import forms
from rlogdata.models import Mandates

class MandateForm(forms.ModelForm):

    class Meta:
        model = Mandates
        fields = '__all__'
