from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('ping', views.ping),
    path('students/', views.students_all),
    path('profs/', views.profs_all),
    path('subjects/', views.subjects_all),
    path('students/<int:pk>', views.StudentsView.as_view()),
    path('profs/<int:pk>', views.ProfsView.as_view()),
    path('subjects/<int:pk>', views.SubjectsView.as_view()),
]
