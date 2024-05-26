from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User as DjangoUser
from django.conf import settings
from .models import User

class MongoBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.get_user_by_username(username)
        if user and password == user.password:
            return self.get_django_user(user)
        return None

    def get_django_user(self, user):
        django_user, created = DjangoUser.objects.get_or_create(
            username=user.username,
            defaults={'password': user.password}
        )
        return django_user

    def get_user(self, user_id):
        try:
            return DjangoUser.objects.get(pk=user_id)
        except DjangoUser.DoesNotExist:
            return None
