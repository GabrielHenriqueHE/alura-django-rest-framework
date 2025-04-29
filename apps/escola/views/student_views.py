from rest_framework import generics, viewsets

from apps.escola.models.student_model import Student
from apps.escola.serializers.student_serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


from apps.escola.models.registration_model import Registration
from apps.escola.serializers.student_registrations_list_serializer import \
    StudentRegistrationsListSerializer


class StudentRegistrationList(generics.ListAPIView):

    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs["pk"])

    serializer_class = StudentRegistrationsListSerializer
