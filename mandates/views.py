from django.shortcuts import render
from .forms import MandateForm

# Create your views here.
def mandateform(request):
    f = MandateForm
    return render(request, 'mandateform.html', {'form': f})
