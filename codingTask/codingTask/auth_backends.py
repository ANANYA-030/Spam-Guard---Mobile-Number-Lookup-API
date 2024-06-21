from django.contrib.auth.backends import BaseBackend
from spamIdentifier.models import RegisteredUser
# from django.contrib.auth import get_user_model
# from django.db.models import Q 

class PhoneBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = RegisteredUser.objects.get(phone_number=phone_number)
            if user.check_password(password):
                return user
        except RegisteredUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return RegisteredUser.objects.get(pk=user_id)
        except RegisteredUser.DoesNotExist:
            return None
    # def authenticate(self, request, phone_number=None, password=None, **kwargs):
    #     User = get_user_model()
    #     try:
    #         user = User.objects.get(
    #             Q(phone_number=phone_number)
    #         )
    #         if user.check_password(password):
    #             return user
    #     except User.DoesNotExist:
    #         return None
    #     return None

    # def get_user(self, user_id):
    #     User = get_user_model()
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None
