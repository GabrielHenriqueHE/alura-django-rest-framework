from rest_framework import serializers

from apps.escola.models.student_model import Student
from apps.escola.validators import StudentValidator


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, data):
        return StudentValidator().validate(data)
