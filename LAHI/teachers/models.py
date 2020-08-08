from django.db import models
from main.models import *
from django import forms


class Student(models.Model):
    name = models.CharField(max_length=100, default=None)
    roll_no = models.IntegerField(unique=True)
    phone = models.CharField(max_length=15, default=None, blank=False, null=False)
    # password = models.CharField(max_length=32, default=None)
    std = models.ForeignKey(Standard, default=None, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name