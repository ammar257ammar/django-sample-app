from django.db import models
from django.urls import reverse

# Create your models here.

class protein(models.Model):

    # Fields
    protein_name = models.CharField("Protein Name", max_length=255)
    uniprot_id = models.CharField("Uniprot ID", max_length=20)
    experimental_method = models.CharField("Experimental Method", max_length=255)
    pdb_resolution = models.FloatField("PDB Resolution")
    deposit_date = models.DateTimeField("Deposit Date", auto_now=True, editable=False)
    revision_date = models.DateTimeField("Revision Date", auto_now_add=True, editable=False)
    number_of_chains = models.IntegerField("Number Of Chains")
    sequence_length = models.IntegerField("Sequence Length")
    molecular_weight = models.FloatField("Molecular Weight")
    atom_count = models.IntegerField("Atom Count")

    class Meta:
        pass

    def __str__(self):
        return str(" - ".join([self.protein_name, self.uniprot_id]))

    def get_absolute_url(self):
        return reverse("proteinapp_protein_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("proteinapp_protein_update", args=(self.pk,))
