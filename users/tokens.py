from django.contrib.auth.tokens import PasswordResetTokenGenerator
# import six
from django.contrib.auth.hashers import make_password
import string
import random
import secrets



# class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return(
#                 six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
#             )
# account_activation_token = AccountActivationTokenGenerator()