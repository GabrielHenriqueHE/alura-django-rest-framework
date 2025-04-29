from django.db import models


class Student(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False)
    email = models.EmailField(blank=False, max_length=100, null=False)
    cpf = models.CharField(blank=False, max_length=11, null=False, unique=True)
    birth_date = models.DateField(null=False)
    phone_number = models.CharField(blank=False, max_length=14, null=False)

    def __str__(self):
        return self.name
