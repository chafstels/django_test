from django.contrib import admin

from university.models import Course, Student, StepCourse

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StepCourse)