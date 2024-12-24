from django.db import models

# Create your models here.
# analysis/models.py

class ExampleModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name