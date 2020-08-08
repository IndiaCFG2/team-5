from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name

class Standard(models.Model):
    standard = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return str(self.standard)

