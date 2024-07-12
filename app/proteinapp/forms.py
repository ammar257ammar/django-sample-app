from django import forms
from . import models

class ProteinForm(forms.ModelForm):
    class Meta:
        model = models.protein
        fields = []
