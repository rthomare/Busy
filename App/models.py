from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    busy = models.BooleanField()
    busy_image = models.CharField(max_length=200)
    not_busy_image = models.CharField(max_length=200)
