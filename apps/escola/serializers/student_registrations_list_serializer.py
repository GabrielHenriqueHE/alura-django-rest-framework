from rest_framework import serializers

from apps.escola.models.registration_model import Registration


class StudentRegistrationsListSerializer(serializers.ModelSerializer):

    course = serializers.ReadOnlyField(source="course.description")
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ["course", "period"]

    def get_period(self, obj):
        return obj.get_period_display()
