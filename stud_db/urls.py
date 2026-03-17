from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='students'),
    path('courses/', views.course_list, name='courses'),
    path('register/', views.register, name='register'),
    path('enrolled/', views.enrolled_list, name='enrolled'),
]