from rest_framework import serializers

from apps.escola.models.registration_model import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"
