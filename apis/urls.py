from django.urls import path

from .views import CertificateAPIView, CertificateDetialAPIView

urlpatterns = [
    path('<int:pk>/', CertificateDetialAPIView.as_view(), name='cert_detail'),
    path('', CertificateAPIView.as_view(), name='cert_list'),
]