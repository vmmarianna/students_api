from django.test import TestCase
from student.models import Student


class TestSimple(TestCase):

    def test_create_student(self):
        Student.objects.create(
            name="Test_Name"
        )

        self.assertGreater(0, Student.objects.count())
