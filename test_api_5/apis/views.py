from rest_framework import status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import *
from apis.serializers import *

class SchoolViewSet(viewsets.GenericViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'name': ['icontains', 'exact'],
    }

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def retreive(self, request, id):
        school = self.get_object()
        return Response()
    
    def update(self, request, id):
        school = self.get_object()
        serializer = self.get_serializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, id):
        school = self.get_object()
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassroomViewset(viewsets.GenericViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'school': ['in', 'exact'],
        'school__name': ['icontains', 'exact']
    }

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def retreive(self, request, id):
        return Response()
    
    def update(self, request, id):
        school = self.get_object()
        serializer = self.get_serializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, id):
        school = self.get_object()
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeacherViewset(viewsets.GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'classrooms': ['in', 'exact'],
        'classrooms__school': ['in', 'exact'],
        'classrooms__school__name': ['icontains', 'exact'],
        'first_name': ['in', 'exact', 'icontains'],
        'last_name': ['in', 'exact', 'icontains'],
        'gender': ['in', 'exact'],
    }

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TeacherDetailSerializer
        return TeacherSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def retrieve(self, request, id):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def update(self, request, id):
        school = self.get_object()
        serializer = self.get_serializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, id):
        school = self.get_object()
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'classroom': ['in', 'exact'],
        'classroom__school': ['in', 'exact'],
        'classroom__school__name': ['icontains', 'exact'],
        'first_name': ['in', 'exact', 'icontains'],
        'last_name': ['in', 'exact', 'icontains'],
        'gender': ['in', 'exact'],
    }

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StudentDetailSerializer
        return StudentSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def retrieve(self, request, id):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def update(self, request, id):
        school = self.get_object()
        serializer = self.get_serializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, id):
        school = self.get_object()
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)