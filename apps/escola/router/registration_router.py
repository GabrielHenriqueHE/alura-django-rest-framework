from rest_framework import routers

from apps.escola.views.registration_views import RegistrationViewSet

registration_router = routers.DefaultRouter()

registration_router.register(
    "registrations", RegistrationViewSet, basename="registrations"
)
