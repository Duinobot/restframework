from django.shortcuts import render
from django.views.generic import ListView
from .models import Certificate
# Create your views here.

class CertificateListView(ListView):
    model = Certificate
    template_name = 'certificate_list.html'