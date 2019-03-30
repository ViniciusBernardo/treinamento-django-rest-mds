from django.db import models


class Teacher(models.Model):

    full_name = models.CharField(max_length=80, blank=False)

    knowledge_area = models.CharField(max_length=80, blank=False)

    date_of_birth = models.DateField()


class Student(models.Model):

    full_name = models.CharField(max_length=80, blank=False)

    date_of_birth = models.DateField()

    registration = models.CharField(max_length=20, blank=False)
