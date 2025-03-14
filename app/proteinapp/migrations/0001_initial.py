# Generated by Django 4.2.13 on 2024-07-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='protein',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proten_name', models.CharField(max_length=255, verbose_name='protein_name')),
                ('uniprot_id', models.CharField(max_length=20, verbose_name='uniprot_id')),
                ('experimental_method', models.CharField(max_length=255, verbose_name='experimental_method')),
                ('pdb_resolution', models.FloatField(verbose_name='pdb_resolution')),
                ('deposit_date', models.DateTimeField(auto_now=True, verbose_name='deposit_date')),
                ('revision_date', models.DateTimeField(auto_now_add=True, verbose_name='revision_date')),
                ('number_of_chains', models.IntegerField(max_length=2, verbose_name='number_of_chains')),
                ('sequence_length', models.IntegerField(max_length=6, verbose_name='sequence_length')),
                ('molecular_weight', models.FloatField(verbose_name='molecular_weight')),
                ('atom_count', models.IntegerField(max_length=6, verbose_name='atom_count')),
            ],
        ),
    ]
