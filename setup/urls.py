from django.contrib import admin
from django.urls import include, path

from apps.escola.router import router

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
