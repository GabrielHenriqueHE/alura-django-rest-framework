from rest_framework import routers

from apps.escola.router.course_router import course_router
from apps.escola.router.registration_router import registration_router
from apps.escola.router.student_router import student_router

router = routers.DefaultRouter()

router.registry.extend(course_router.registry)
router.registry.extend(student_router.registry)
router.registry.extend(registration_router.registry)
