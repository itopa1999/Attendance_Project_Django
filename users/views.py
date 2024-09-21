#built-in imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout,get_user_model,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import *
from django.core.exceptions import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import string
from django.db.models import Q
from datetime import date,timedelta
# import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

#app imports
from .models import *



def login_user(request):
    referer_url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('index')




def index(request):

    return render(request, 'index.html')


def students(request):
    try:
        student = Student.objects.all()
    except:
        return JsonResponse("student is not found")
    context={"student":student}
    return render(request, 'students.html', context)


def sign_in(request):
    try:
        student = Sign_In.objects.all()
    except:
        return JsonResponse("student is not found")
    context={"student":student}
    return render(request, 'sign_in.html', context)


def sign_out(request):
    try:
        student = Sign_Out.objects.all()
    except:
        return JsonResponse("student is not found")
    context={"student":student}
    return render(request, 'sign_out.html', context)


def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except:
        return JsonResponse("student is not found")
    context={"student":student}
    return render(request, 'student_detail.html', context)









def count_mode(request):
    sign_out =+ 1
    sign_in =+ 1
    data = {
        'sign_out':sign_out,
        'sign_in':sign_in,
    }
    return JsonResponse(data)