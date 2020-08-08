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

class MediaFile(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=10)
    media = models.FileField(upload_to='', null=True, verbose_name="")

    def __str__(self):
        return self.title

