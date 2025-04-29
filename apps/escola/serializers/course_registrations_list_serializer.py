from rest_framework import serializers

from apps.escola.models import Registration


class CourseRegistrationsListSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source="student.name")

    class Meta:
        model = Registration
        fields = ["student"]
