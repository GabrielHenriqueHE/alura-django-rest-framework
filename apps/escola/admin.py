from django.contrib import admin

from apps.escola.models.course_model import Course
from apps.escola.models.registration_model import Registration
from apps.escola.models.student_model import Student


class Students(admin.ModelAdmin):
    list_display = ["id", "name", "email", "cpf", "birth_date", "phone_number"]
    list_display_links = ["id", "name"]
    list_per_page = 20
    search_fields = ["name"]


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ["id", "code", "description", "level"]
    list_display_links = ["id", "code", "description"]
    search_fields = ["code", "description"]


admin.site.register(Course, Courses)


class Registrations(admin.ModelAdmin):
    list_display = ["id", "student", "course", "period"]
    list_display_links = ["id", "student"]
    search_fields = ["student"]


admin.site.register(Registration, Registrations)
