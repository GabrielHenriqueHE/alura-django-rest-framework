from apps.escola.models.course_model import Course
from apps.escola.serializers.course_serializer import CourseSerializer

from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer