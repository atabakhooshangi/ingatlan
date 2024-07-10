from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from src.users.models.choices.choices import GenderChoiceType
from src.users.models.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=65, unique=True, blank=False, null=False)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=20, blank=True, null=True,
                                    unique=True)

    first_name = models.CharField(verbose_name='First Name', max_length=75, null=True, blank=True, default="")
    last_name = models.CharField(verbose_name='Last Name', max_length=75, null=True, blank=True, default="")
    province = models.CharField(verbose_name='Province', max_length=40, null=True, blank=True, default="")
    city = models.CharField(verbose_name='City', max_length=40, null=True, blank=True, default="")
    birthday = models.CharField(verbose_name='Birthday', max_length=10, null=True, blank=True, default="")
    gender = models.CharField(verbose_name='Gender', choices=GenderChoiceType, max_length=10, null=True, blank=True,
                              default="")
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f' {self.first_name} {self.last_name} - {self.phone_number}'
        return f'{self.phone_number}'

    @property
    def profile_done(self):
        fields = ['first_name', 'last_name', 'province', 'city', 'birthday', 'gender']
        for field_name in fields:
            if getattr(self, field_name) == "" or None:
                return False
        return True

    #
    # @property
    # def tokens(self):
    #     token = RefreshToken.for_user(self)
    #     data = {
    #         'refresh': str(token),
    #         'access': str(token.access_token)
    #     }
    #     return data

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('date_joined',)
