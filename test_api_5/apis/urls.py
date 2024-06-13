from django.urls import path, include
from rest_framework import routers

from apis import views

router = routers.DefaultRouter()
router.register(r'school', views.SchoolViewSet, basename='school')
router.register(r'classroom', views.ClassroomViewset, basename='classroom')
router.register(r'teacher', views.TeacherViewset, basename='teacher')
router.register(r'student', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', include([
        path('', include(router.urls)),
    ])),
]