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
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField(blank=True)
    question_image = models.ImageField(upload_to='questions/', blank=True, null=True)

    option1 = models.CharField(max_length=255, blank=True)
    option2 = models.CharField(max_length=255, blank=True)
    option3 = models.CharField(max_length=255, blank=True)
    option4 = models.CharField(max_length=255, blank=True)

    correct_option = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Question for {self.exam.title}"
