# from django.contrib import admin
# from django.urls import path
# from exams import views as exam_views
# from results import views as result_views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     path('', exam_views.home, name='home'),
#     path('subjects/<int:subject_id>/', exam_views.exam_list, name='exam_list.html'),
#     path('exam/<int:exam_id>/', exam_views.start_exam, name='start_exam'),
#
#     path('result/<uuid:result_id>/', result_views.result_view, name='result'),
#
#     path('search/', result_views.search_result, name='search'),
# ]
# from django.contrib.auth import views as auth_views
#
# urlpatterns += [
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]
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
