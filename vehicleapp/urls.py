from django.urls import path
from .views import *

urlpatterns = [
   path('',reports),
   path('download-csv/', generate_csv, name='download_csv'),
   path('download-pdf/', generate_pdf, name='download_pdf'),
   path('total-miles/', total_miles_driven, name='total_miles'),
]