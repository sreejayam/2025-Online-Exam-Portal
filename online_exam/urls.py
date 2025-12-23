
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as accounts_views
from exams import views as exams_views
from results import views as results_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),

    # Home
    path('', exams_views.home, name='home'),

    # Subjects
    path('subjects/<int:subject_id>/', exams_views.exam_list, name='exam_list'),

    # Exam
    path('exam/<int:exam_id>/', exams_views.start_exam, name='start_exam'),

    # Result
    path('result/<uuid:result_id>/', results_views.result_view, name='result'),
path('register/', accounts_views.register_view, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
