from django.urls import path, include
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('count_mode', count_mode, name='count_mode'),
    path('students', students, name='students'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out'),
    path('student_detail/<str:pk>', student_detail, name='student_detail'),
    path('login', login_user, name='login'),
    path('login', login_user, name='login'),
    path('login', login_user, name='login'),
    path('login', login_user, name='login'),

]