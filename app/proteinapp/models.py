from django.db import models
from django.urls import reverse

# Create your models here.

class protein(models.Model):

    # Fields
    protein_name = models.CharField("protein_name", max_length=255)
    uniprot_id = models.CharField("uniprot_id", max_length=20)
    experimental_method = models.CharField("experimental_method", max_length=255)
    pdb_resolution = models.FloatField("pdb_resolution")
    deposit_date = models.DateTimeField("deposit_date", auto_now=True, editable=False)
    revision_date = models.DateTimeField("revision_date", auto_now_add=True, editable=False)
    number_of_chains = models.IntegerField("number_of_chains")
    sequence_length = models.IntegerField("sequence_length")
    molecular_weight = models.FloatField("molecular_weight")
    atom_count = models.IntegerField("atom_count")

    class Meta:
        pass

    def __str__(self):
        return str(" - ".join([self.protein_name, self.uniprot_id]))

    def get_absolute_url(self):
        return reverse("proteinapp_protein_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("proteinapp_protein_update", args=(self.pk,))
