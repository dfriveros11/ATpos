from django import forms
from pay.models import Pay

class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = "__all__"