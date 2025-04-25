from rest_framework import viewsets

from apps.escola.models.registration_model import Registration
from apps.escola.serializers.registration_serializer import \
    RegistrationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
