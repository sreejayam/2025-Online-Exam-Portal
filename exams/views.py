from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Subject, Exam, Question
from results.models import ExamResult
import random

from results.models import ExamResult

# @login_required
# def home(request):
#     subjects = Subject.objects.all()
#     result = None
#
#     if request.GET.get('result_id'):
#         result = ExamResult.objects.filter(
#             result_id=request.GET['result_id']
#         ).first()
#
#     return render(request, 'home.html', {
#         'subjects': subjects,
#         'result': result
#     })
from results.models import ExamResult

@login_required
def home(request):
    subjects = Subject.objects.all()

    # ✅ latest exam attempt of logged-in user
    latest_result = ExamResult.objects.filter(
        user=request.user
    ).order_by('-completed_at').first()

    # ✅ search by exam ID (optional)
    searched_result = None
    if request.GET.get('result_id'):
        searched_result = ExamResult.objects.filter(
            result_id=request.GET['result_id']
        ).first()

    return render(request, 'home.html', {
        'subjects': subjects,
        'latest_result': latest_result,
        'result': searched_result
    })


@login_required
def exam_list(request, subject_id):
    today = timezone.now().date()
    exams = Exam.objects.filter(
        subject_id=subject_id,
        start_date__lte=today,
        end_date__gte=today
    )
    return render(request, 'exam_list.html', {'exams': exams})


@login_required

def start_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    # ✅ get all questions
    all_questions = list(Question.objects.filter(exam=exam))

    if not all_questions:
        return render(request, 'exam.html', {
            'exam': exam,
            'questions': [],
            'error': 'No questions available for this exam.'
        })

    # ✅ ensure no overflow
    question_count = min(exam.total_questions, len(all_questions))

    # ✅ slice instead of random.sample (SAFE)
    questions = all_questions[:question_count]

    if request.method == "POST":
        score = 0
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected and int(selected) == q.correct_option:
                score += 1

        result = ExamResult.objects.create(
            user=request.user,
            exam=exam,
            score=score,
            total=question_count
        )
        return redirect('result', result.result_id)

    return render(request, 'exam.html', {
        'exam': exam,
        'questions': questions
    })