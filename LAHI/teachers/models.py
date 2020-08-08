from django.db import models
from main.models import *
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    phone = models.CharField(max_length=15, default=None)
    std = models.ForeignKey(Standard, default=None, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return str(self.user)