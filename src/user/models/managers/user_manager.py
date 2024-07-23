from django.contrib.auth.models import BaseUserManager
from rest_framework import exceptions


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    def create_user(self, email, password=None):
        if not email:
            raise exceptions.ValidationError({'Email': ['Email is Required.']})

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise exceptions.ValidationError({'Password': ['Password is Required.']})

        admin = self.create_user(
            email=self.normalize_email(email)
        )

        admin.set_password(password)

        admin.is_active = True
        admin.is_staff = True
        admin.is_superuser = True
        admin.is_admin = True
        admin.save(using=self._db)
        return admin
