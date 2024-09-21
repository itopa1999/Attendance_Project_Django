from django.shortcuts import redirect
from django.contrib import messages
from users.models import User
from django.contrib.auth.models import Group
from django.utils import timezone
from datetime import date



# def agent_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group_name = request.user.groups.first().name if request.user.groups.exists() else None
#         if group_name in ['admin', 'manager']:
#             return redirect('decline')
#         return view_func(request, *args, **kwargs)
#     return wrapper_function


# def manager_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group_name = request.user.groups.first().name if request.user.groups.exists() else None
#         if group_name in ['admin','agent','superadmin']:
#             return redirect('decline')
#         return view_func(request, *args, **kwargs)
#     return wrapper_function


# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group_name = request.user.groups.first().name if request.user.groups.exists() else None
#         if group_name in ['manager','agent','superadmin']:
#             return redirect('decline')
#         return view_func(request, *args, **kwargs)
#     return wrapper_function


# def superadmin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group_name = request.user.groups.first().name if request.user.groups.exists() else None
#         if group_name in ['manager','agent','admin']:
#             return redirect('decline')
#         return view_func(request, *args, **kwargs)
#     return wrapper_function


# def complete_profile(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         user = request.user
#         if user.groups.filter(name='agent'):
#             if not user.country or not user.phone or not user.state or not user.city:
#                 messages.info(request, ' complete your profile to view page')
#                 return redirect('agent-dashboard')
#             else:
#                 return view_func(request, *args, **kwargs)
#         else:
#             return view_func(request, *args, **kwargs)

#     return wrapper_function



# def group_permission_required(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         user = request.user
#         if user.groups.filter(name='agent').exists() or user.groups.filter(name='manager').exists():
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('decline')
#     return wrapper_function



# def group_permission_required2(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         user = request.user
#         if user.groups.filter(name='admin').exists() or user.groups.filter(name='manager').exists():
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('decline')
#     return wrapper_function



# def group_permission_required3(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         user = request.user
#         if user.groups.filter(name='admin').exists() or user.groups.filter(name='superadmin').exists():
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('decline')
#     return wrapper_function