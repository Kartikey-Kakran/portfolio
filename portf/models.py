from os import name
from django.db import models

# Create your models here.
class down(models.Model):
    name=models.FileField()