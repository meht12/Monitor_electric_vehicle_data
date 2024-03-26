from django.shortcuts import render,HttpResponse
from .models import vehicle
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.http import HttpResponse
# show the data 
def reports(request):
    data=vehicle.objects.all()
    return render (request,'vehicle.html',{'report':data})


# downlaod the csv file 

def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vehicle_data.csv"'
    
    # Write CSV headers
    writer = csv.writer(response)
    writer.writerow(['License Plate', 'Make', 'VIN', 'Model', 'Type', 'Creation Date', 'Miles Driven'])
    
    # Write CSV data
    vehicles = vehicle.objects.all()
    for vehicle_instance in vehicles:
        writer.writerow([
            vehicle_instance.License_plate,
            vehicle_instance.make,
            vehicle_instance.vin,
            vehicle_instance.model,
            vehicle_instance.types,
            vehicle_instance.creation_date,
            vehicle_instance.miles_driven,
        ])
    
    return response

# To generate PDF

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="vehicle_data.pdf"'
    
    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    
    # Table data
    vehicles = vehicle.objects.all()
    data = [['License Plate', 'Make', 'VIN', 'Model', 'Type', 'Creation Date', 'Miles Driven']]
    for vehicle_instance in vehicles:
        data.append([
            vehicle_instance.License_plate,
            vehicle_instance.make,
            vehicle_instance.vin,
            vehicle_instance.model,
            vehicle_instance.types,
            str(vehicle_instance.creation_date),
            vehicle_instance.miles_driven,
        ])
    
    # Create a table
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                               ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    
    # Add table to the PDF document
    doc.build([table])
    
    return response