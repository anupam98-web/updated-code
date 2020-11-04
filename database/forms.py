from django import forms

from .models import Mandate

class MandateForm(forms.ModelForm):

    class Meta:
        model = Mandate
        fields = '__all__'

