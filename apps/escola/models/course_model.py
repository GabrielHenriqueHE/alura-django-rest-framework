from django.core.validators import MinLengthValidator
from django.db import models


class Course(models.Model):
    LEVEL = (("B", "Basic"), ("I", "Intermediary"), ("A", "Advanced"))

    code = models.CharField(
        blank=False,
        max_length=10,
        null=False,
        unique=True,
        validators=[MinLengthValidator(3)],
    )
    description = models.CharField(blank=False)
    level = models.CharField(blank=False, choices=LEVEL, default="B", null=False)

    def __str__(self):
        return self.code
