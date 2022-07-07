from rest_framework import generics, permissions

from certificates.models import Certificate
from .serializers import CertificateSerializer
from django.shortcuts import render

from .permissions import IsVendorOrReadOnly

# Create your views here.
class CertificateAPIView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateDetialAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = (IsVendorOrReadOnly,)