from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class Crew(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "crews"

        def __str__(self):
            return self.name
