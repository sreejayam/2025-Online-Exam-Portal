from django.shortcuts import render, get_object_or_404
from .models import ExamResult

def result_view(request, result_id):
    result = get_object_or_404(ExamResult, result_id=result_id)
    return render(request, 'result.html', {'result': result})


def search_result(request):
    result = None
    if request.GET.get('result_id'):
        result = ExamResult.objects.filter(
            result_id=request.GET['result_id']
        ).first()
    return render(request, 'search.html', {'result': result})

