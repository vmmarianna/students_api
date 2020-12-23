from rest_framework import serializers

from student.models import Student, Prof, Subject


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['pk', 'name']


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = ['pk', 'name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['pk', 'subject_name', 'prof', 'student']
