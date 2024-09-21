from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model



User = get_user_model()

class LoginBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user = None
        if email is not None:
            user =User.objects.filter(email=email).first()
        if user is None:
            user =User.objects.filter(profile_code=email).first()
        if user is None:
            user =User.objects.filter(username=email).first()
        if user and user.check_password(password):
            return user 
        else:
            return None
            