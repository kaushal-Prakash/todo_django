from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('time/<int:offset>/', views.time, name='time'),
    path('age-calculator/<int:year>/', views.age_calculator, name='age_calculator'),
]