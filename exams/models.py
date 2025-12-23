import uuid
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    total_questions = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title




class Question(models.Model):
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    question_text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='questions/', blank=True, null=True)

    option1 = models.CharField(max_length=255, blank=True, null=True)
    option1_image = models.ImageField(upload_to='options/', blank=True, null=True)

    option2 = models.CharField(max_length=255, blank=True, null=True)
    option2_image = models.ImageField(upload_to='options/', blank=True, null=True)

    option3 = models.CharField(max_length=255, blank=True, null=True)
    option3_image = models.ImageField(upload_to='options/', blank=True, null=True)

    option4 = models.CharField(max_length=255, blank=True, null=True)
    option4_image = models.ImageField(upload_to='options/', blank=True, null=True)

    correct_option = models.IntegerField(choices=[
        (1, 'Option 1'),
        (2, 'Option 2'),
        (3, 'Option 3'),
        (4, 'Option 4'),
    ])
