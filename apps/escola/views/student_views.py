from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters

from apps.escola.models.student_model import Student
from apps.escola.serializers.student_serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'name']
    search_fields = ['name', 'cpf']


from apps.escola.models.registration_model import Registration
from apps.escola.serializers.student_registrations_list_serializer import \
    StudentRegistrationsListSerializer


class StudentRegistrationList(generics.ListAPIView):

    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs["pk"])

    serializer_class = StudentRegistrationsListSerializer
