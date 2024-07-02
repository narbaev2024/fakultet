from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name

class Professor(models.Model):
    user = models.CharField(max_length=32, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    bio = models.TextField()

    def __str__(self):
        return self.user

class Student(models.Model):
    user = models.CharField(max_length=32, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField()
    graduation_date = models.DateTimeField()

    def __str__(self):
        return self.user

class Cours(models.Model):
    name = models.CharField(max_length=32)
    code = models.IntegerField()
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name
