from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('ping', views.ping),
    path('simple_post', views.simple_post),

]