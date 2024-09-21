from django.db import models
from django.contrib.auth.models import Group, AbstractUser
from .manager import MyUserManager
import random
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from PIL import Image
from io import BytesIO
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.

def generate_seria_nubmer():
    # Generate random profile codes starting with "SN"
    codes = "SN" + str(random.randint(10000000, 99999999))
    return codes

class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), blank=False, unique=True)
    profile_code = models.CharField(max_length=100)
    access = models.BooleanField(default=True)
    def save(self, *args, **kwargs) -> None:
        while not self.profile_code:
            profile_code = generate_seria_nubmer()
            objects_with_similar_profile_code = User.objects.filter(
                profile_code=profile_code
            )
            if not objects_with_similar_profile_code:
                self.profile_code = profile_code

        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ["-date_joined"]
        indexes = [
            models.Index(fields=["-date_joined"]),
        ]

    def __str__(self):
        return f"{self.username}"

    objects = MyUserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name","last_name"]
    
    

class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    class Meta:
        ordering = ["-is_valid"]

    @property
    def has_expired(self):
        """
        Checks if token has expired
        Set token to expire after 600 seconds (10 minutes)
        """

        delta = timezone.now() - self.time_created
        return delta.seconds > 600

    class Meta:
        ordering = ["-is_valid"]
        indexes = [
            models.Index(fields=["-is_valid"]),
        ]

    
    def __str__(self):
        return str(self.token)
    
    

class Student(models.Model):
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    matric_no = models.CharField(max_length=50, null=True,blank=True)
    department = models.CharField(max_length=50, null=True,blank=True)
    faculty = models.CharField(max_length=50, null=True,blank=True)
    profile_code = models.CharField(max_length=50, null=True,blank=True)
    gender = models.CharField(max_length=50, null=True,blank=True)
    enroll = models.BooleanField(default=False)
    profile_pic = models.ImageField(null=True,default='profile_pic.jpg', blank=True)

    def save(self, *args, **kwargs) -> None:
        while not self.profile_code:
            profile_code = generate_seria_nubmer()
            objects_with_similar_profile_code = Student.objects.filter(
                profile_code=profile_code
            )
            if not objects_with_similar_profile_code:
                self.profile_code = profile_code

        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ["-id"]
        indexes = [
            models.Index(fields=["-id"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Sign_In(models.Model):
    student = student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"



class Sign_Out(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"
    


class FingerPrint(models.Model):
    student = student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    field1 = models.CharField(max_length=50, null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"