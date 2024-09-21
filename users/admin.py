from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Sign_In)
admin.site.register(Sign_Out)

# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         "username",
#         "email",
#         "phone",
#         "first_name",
#         "last_name",
#     )



# admin.site.register(User, UserAdmin)


# class OtpAdmin(admin.ModelAdmin):
#     list_display = ("user", "token", "is_valid", "has_expired")


# admin.site.register(Otp, OtpAdmin)

# admin.site.register(Routing)

