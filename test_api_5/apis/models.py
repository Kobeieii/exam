from django.db import models

class GenderEnum(models.TextChoices):
    FEMALE = 'f'
    MALE = 'm'

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=10)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school'

class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.IntegerField()
    room = models.IntegerField()
    school = models.ForeignKey(School, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('grade', 'room', 'school'),)
        db_table = 'classroom'

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GenderEnum.choices)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('first_name', 'last_name'),)
        db_table = 'teacher'

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GenderEnum.choices)
    classroom = models.ForeignKey(Classroom, models.DO_NOTHING, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('first_name', 'last_name'),)
        db_table = 'student'

