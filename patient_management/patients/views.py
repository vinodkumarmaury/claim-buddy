from django.core.paginator import Paginator
from .models import Patient
from django.shortcuts import render
def patient_list(request):
    query = request.GET.get('q')
    patient_list = Patient.objects.all()
    if query:
        patient_list = patient_list.filter(full_name__icontains=query)
    paginator = Paginator(patient_list, 5)
    page_number = request.GET.get('page')
    patients = paginator.get_page(page_number)
    return render(request, 'patients/patient_list.html', {'patients': patients, 'query': query})
