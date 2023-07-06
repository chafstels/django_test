from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class StepCourse(models.Model):
    step = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses', related_query_name='courses')
    step_course = models.OneToOneField(StepCourse, related_name='courses_step', related_query_name='courses_step',
                                       on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name