from rest_framework import routers

from apps.escola.views.course_views import CourseViewSet

course_router = routers.DefaultRouter()

course_router.register("courses", CourseViewSet, basename="courses")
