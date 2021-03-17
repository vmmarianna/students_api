from django.db import models


class Prof(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Prof: <{self.pk}> {self.name}'


class Student(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Student: <{self.pk}> {self.name}'


class Subject(models.Model):
    subject_name = models.CharField(max_length=255, null=True, blank=True)
    prof = models.ForeignKey(Prof, models.SET_NULL, null=True, blank=True)
    student = models.ManyToManyField('Student', related_name='subject')

    def __str__(self):
        return f'Subject: <{self.pk}> {self.subject_name}'


# class Prof(models.Model):
#     prof_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'prof'
#
#
# class Students(models.Model):
#     student_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'students'
#
#
# class Subjects(models.Model):
#     subject_id = models.AutoField(primary_key=True)
#     subject_name = models.CharField(max_length=255)
#     prof = models.ForeignKey(Prof, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'subjects'
#
#
# class SubjectsStudents(models.Model):
#     record_id = models.AutoField(primary_key=True)
#     student = models.ForeignKey(Students, models.DO_NOTHING)
#     subject = models.ForeignKey(Subjects, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'subjects_students'
