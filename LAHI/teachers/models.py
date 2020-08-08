from django.db import models
from main.models import *

class Student(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    std = models.ForeignKey(Standard, default=None, on_delete=models.SET_DEFAULT)

    # def __str__(self):
    #     return self.name