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

class Subject(models.Model):
    sub = models.CharField(max_length=100)

    def __str__(self):
        return self.sub

class FileType(models.Model):
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.file_type

class MediaFile(models.Model):
    std = models.ForeignKey(Standard, default=None, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)
    file_type = models.ForeignKey(FileType, default=None, on_delete=models.DO_NOTHING)
    media = models.FileField(upload_to='', null=True, verbose_name="")

    def __str__(self):
        return str(self.media)

