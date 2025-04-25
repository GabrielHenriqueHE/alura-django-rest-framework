from django.db import models


class Course(models.Model):
    LEVEL = (("B", "Basic"), ("I", "Intermediary"), ("A", "Advanced"))

    code = models.CharField(blank=False, max_length=10, null=False)
    description = models.CharField(blank=False)
    level = models.CharField(blank=False, choices=LEVEL, default="B", null=False)

    def __str__(self):
        return self.code
