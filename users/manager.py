from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser True.")

        user = self.create_user(
            username, email, password=password, **extra_fields)
        admin_group, created = Group.objects.get_or_create(name="admin")
        user.groups.add(admin_group)
        user.verified = True
        user.save(using=self._db)
        return user
