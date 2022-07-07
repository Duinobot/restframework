from rest_framework import serializers

from certificates.models import Certificate

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('imei', 'content')