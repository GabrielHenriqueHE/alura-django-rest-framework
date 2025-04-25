from rest_framework import routers

from apps.escola.views.student_views import StudentViewSet

student_router = routers.DefaultRouter()

student_router.register("students", StudentViewSet, basename="students")
