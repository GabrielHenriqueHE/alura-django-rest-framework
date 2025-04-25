from rest_framework import serializers

from apps.escola.models.course_model import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
