from django.urls import path
from .views import *

urlpatterns = [
   path('reports/',reports),
    path('download-csv/', generate_csv, name='download_csv'),
     path('download-pdf/', generate_pdf, name='download_pdf'),
]