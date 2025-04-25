from rest_framework import viewsets

from apps.escola.models.student_model import Student
from apps.escola.serializers.student_serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
