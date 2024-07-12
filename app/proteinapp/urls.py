from django.urls import path

from . import views

urlpatterns = (
    path("proteinapp/protein/", views.ProteinListView.as_view(), name="proteinapp_protein_list"),
    path("proteinapp/protein/create/", views.ProteinCreateView.as_view(), name="proteinapp_protein_create"),
    path("proteinapp/protein/detail/<int:pk>/", views.ProteinDetailView.as_view(), name="proteinapp_protein_detail"),
    path("proteinapp/protein/update/<int:pk>/", views.ProteinUpdateView.as_view(), name="proteinapp_protein_update"),
    path("proteinapp/protein/delete/<int:pk>/", views.ProteinDeleteView.as_view(), name="proteinapp_protein_delete"),
)