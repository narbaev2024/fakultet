from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)

class Fakultet(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name

class Professor(models.Model):
    user = models.CharField(max_length=32, unique=True)
    department = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user

class Student(models.Model):
    user = models.CharField(max_length=32, unique=True)
    department = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField()
    graduation_date = models.DateTimeField()

    def __str__(self):
        return self.user

class Course(models.Model):
    name = models.CharField(max_length=32)
    code = models.IntegerField()
    description = models.TextField()
    department = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cabinet(models.Model):
    room_number = models.PositiveIntegerField(verbose_name="Number")
    building = models.CharField(max_length=16)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.room_number

class Raspisanie(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=32)

    def __str__(self):
        return self.course

class Zapis_na_course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField()
    grade = models.CharField(max_length=32)

    def __str__(self):
        return self.student

class Dz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Sdacha_dz(models.Model):
    assignment = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateTimeField()
    grade = models.PositiveIntegerField()
    feedback = models.TextField()

    def __str__(self):
        return self.assignment
