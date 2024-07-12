from django.contrib import admin
from django import forms

from . import models

class proteinAdminForm(forms.ModelForm):

    class Meta:
        model = models.protein
        fields = "__all__"


class proteinAdmin(admin.ModelAdmin):
    form = proteinAdminForm
    list_display = [
        "protein_name",
        "uniprot_id",
        "pdb_resolution",
        "deposit_date",
        "revision_date"
    ]
    readonly_fields = [
        "deposit_date",
        "revision_date"
    ]

admin.site.register(models.protein, proteinAdmin)