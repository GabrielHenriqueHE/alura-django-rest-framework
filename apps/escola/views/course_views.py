from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters

from apps.escola.models.course_model import Course
from apps.escola.serializers.course_serializer import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'code', 'name']
    search_fields = ['code', 'name']


from apps.escola.models.registration_model import Registration
from apps.escola.serializers.course_registrations_list_serializer import \
    CourseRegistrationsListSerializer


class CourseRegistrationList(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs["pk"])

    serializer_class = CourseRegistrationsListSerializer
