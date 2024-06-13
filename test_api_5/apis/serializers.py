from rest_framework import serializers
from apis.models import *

class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        exclude = ['created_at', 'updated_at']

class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        exclude = ['created_at', 'updated_at']

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        exclude = ['created_at', 'updated_at']

class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True)

    class Meta:
        model = Teacher
        exclude = ['created_at', 'updated_at']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at']

class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer()

    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at']