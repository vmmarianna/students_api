from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from student.models import Student, Subject, Prof
from student.serializers import StudentSerializer, SubjectSerializer, ProfSerializer


@api_view(['GET'])
def ping(request):
    data = request.data
    return Response({'message': 'pong', 'data': data})


class StudentsView(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = self.serializer_class(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = self.serializer_class(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def students_all(request):
    students = Student.objects.all()
    return Response([StudentSerializer(student).data for student in students])


@api_view(['GET'])
def profs_all(request):
    profs = Prof.objects.all()
    return Response([ProfSerializer(prof).data for prof in profs])


@api_view(['GET'])
def subjects_all(request):
    subjects = Subject.objects.all()
    return Response([SubjectSerializer(subject).data for subject in subjects])


class SubjectsView(APIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subject = self.get_object(pk)
        serializer = self.serializer_class(subject)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subject = self.get_object(pk)
        serializer = self.serializer_class(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfsView(APIView):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = self.serializer_class(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = self.serializer_class(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
