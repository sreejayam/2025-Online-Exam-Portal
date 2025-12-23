from django.db import models
from django.contrib.auth.models import User
from exams.models import Exam
import uuid

class ExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    score = models.PositiveIntegerField()
    total = models.PositiveIntegerField()


    result_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exam.title}"