from django.urls import include, path

from apps.escola.router import router
from apps.escola.views.course_views import CourseRegistrationList
from apps.escola.views.student_views import StudentRegistrationList

urlpatterns = [
    path("", include(router.urls)),
    path("students/<int:pk>/registrations", StudentRegistrationList.as_view()),
    path("courses/<int:pk>/registrations", CourseRegistrationList.as_view()),
]
