from django import forms
from method.models import Method

class MethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = "__all__"