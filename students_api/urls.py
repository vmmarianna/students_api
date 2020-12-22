from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


app_name = 'students_api'

urlpatterns = [
    path('api/', include('student.urls', namespace='student')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]