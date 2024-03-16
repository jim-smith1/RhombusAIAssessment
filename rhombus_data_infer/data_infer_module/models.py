from django.db import models

# Create your models here.

class FileSchema(models.Model):
    column_name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=100)