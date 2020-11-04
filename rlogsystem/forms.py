from django.forms import ModelForm
from rlogdata.models import Agency

class AgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'
