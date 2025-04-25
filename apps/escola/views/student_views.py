from apps.escola.models.student_model import Student
from apps.escola.serializers.student_serializer import StudentSerializer

from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer